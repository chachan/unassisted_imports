Unassited import of classes controlled by envvars

# Build

    > docker build -t unassisted_imports:local .

# Run

    > docker run -it --rm unassisted_imports:local
    [{'cls': <class 'classes.class1.Class1'>, 'name': 'class1'}]