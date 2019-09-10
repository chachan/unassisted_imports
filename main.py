''' Unassited import demo '''
import os

import classes


def main():
    ''' import subclasses of ClassBase from `classes` directory '''
    for each in os.listdir(os.path.dirname(classes.__file__)):
        if each.endswith('.py') and each != '__init__.py':
            __import__('classes.{}'.format(each[:-3]))
    subclasses = classes.base.ClassBase.__subclasses__()

    defined_classes = []
    for _class in os.environ.get('CLASSES', []).split(','):
        if os.environ.get('{}_ENABLED'.format(_class.upper()), '0') == '1': # is this class enabled?
            if _class.lower() in [each.__name__.lower() for each in subclasses]:
                defined_class = {
                    'cls': subclasses[[each.__name__.lower() for each in subclasses].index(_class.lower())],
                    'name': _class
                }
                defined_classes.append(defined_class)
            else:
                print('Class {} is marked as enabled but class to process it was not found'.format(_class))
    print(defined_classes)

if __name__ == "__main__":
    main()
