#include <Python.h>

/* Implementation */

static PyObject* say_hello(PyObject* self, PyObject* args) {
    const char* name;

    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;

    printf("Hello %s!\n", name);
    Py_RETURN_NONE;
}

static PyObject* version(PyObject* self) {
    return Py_BuildValue("s", "Version 1.0");
}


/* Python Binding Definitions */

static PyMethodDef HelloMethods[] = {
     {"say_hello", say_hello, METH_VARARGS, "Greet somebody."},
     {"version"}, (PyCFunction)version, METH_NOARGS, "returns the version"},
     {NULL, NULL, 0, NULL}
};

static struct PyModuleDef hello = {
    PyModuleDef_HEAD_INIT,
    "hello",			/* name of module */
    "",					/* module documentation, may be NULL */
    -1,					/* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    HelloMethods
};

PyMODINIT_FUNC PyInit_hello(void) {
    return PyModule_Create(&hello);
}