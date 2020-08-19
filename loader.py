import importlib

class ClassLoader(object):

    @staticmethod
    def instantiate_class(class_string):
        processor_path = class_string.strip()

        last_dot = processor_path.rfind(".")
        module_path = processor_path[:last_dot]
        class_name = processor_path[last_dot+1:]

        imported_module = importlib.import_module(module_path)
        new_class = getattr(imported_module, class_name)
        return new_class