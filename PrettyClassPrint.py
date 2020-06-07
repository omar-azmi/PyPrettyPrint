import os

def hex_id(obj):
	return hex(id(obj));

def str_type(obj):
	type_str = str(type(obj));
	def find(string, char):
		return [i for i, letter in enumerate(string) if letter == char];
	try:
		[a,b] = find(type_str, "\'");
		return type_str[a+1:b];
	except:
		return "unknown";


class PrettyClassPrint:
	display_properties = ["__name__", "__repr__", str_type, hex_id];
	display_portions = [0.25, 0.25, 0.25, 0.25];
	display_vertical_separator = " | ";
	display_horizontal_separator = "\u2014";
	
	@classmethod
	def print_single_obj_properties(cls, obj):
		output = [];
		for prop in cls.display_properties:
			try:
				if isinstance(prop, str):
					#We're accessing a class property with obj.__getattribute__("name of property") or getattr(obj, "name of property")
						output += [str(getattr(obj, prop))];
				else:
					#We're passing obj to a function with prop(obj)
					output += [str(prop(obj))];
			except:
				output += ["unknown"];
		return output
	
	@classmethod
	def pretty_print(cls, obj):
		obj_attrs_str = [attr for attr in dir(obj) if not(attr.startswith("__") and attr.endswith("__"))];
		obj_attrs = [getattr(obj, attr) for attr in obj_attrs_str];
		obj_attrs_properties = [cls.print_single_obj_properties(obj_attr) for obj_attr in obj_attrs];		
		terminal_cols, terminal_rows = os.get_terminal_size();
		terminal_cols, terminal_rows = terminal_cols - 1, terminal_rows - 1;
		display_portions_len = [int(terminal_cols*dp - len(cls.display_vertical_separator)) for dp in cls.display_portions];

		def stream_print(string_list):
			print_this_recursion = [""]*len(string_list);
			print_next_recursion = [""]*len(string_list);
			for i, string in enumerate(string_list):
				if len(string) > display_portions_len[i]:
					print_this_recursion[i] = string[0:display_portions_len[i]];
					print_next_recursion[i] = string[display_portions_len[i]:];
				else:
					print_this_recursion[i] = string + " "*(display_portions_len[i]-len(string));
			print(cls.display_vertical_separator.join(print_this_recursion));
			if not(all([s == "" for s in print_next_recursion])):
				stream_print(print_next_recursion);
		
		display_property_names = [];
		for prop in cls.display_properties:
			if isinstance(prop, str):
				display_property_names += [prop];
			else:
				display_property_names += [prop.__name__];

		print((cls.display_horizontal_separator)*(int(float(terminal_cols)/len(cls.display_horizontal_separator))));
		stream_print(display_property_names);
		print((cls.display_horizontal_separator)*(int(float(terminal_cols)/len(cls.display_horizontal_separator))));
		for obj_attr_prop in obj_attrs_properties:
			#Printing each attribute's properties in an organized manner
			stream_print(obj_attr_prop);