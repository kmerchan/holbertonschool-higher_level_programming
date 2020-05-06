#include <Python.h>

/**
 * print_python_list_info - function to print basic info about Python lists
 * @p: input pointer to PyObject or the Python list to print info about
 */

void print_python_list_info(PyObject *p)
{
	ssize_t len = PyList_Size(p);

	printf("[*] Size of the Python list = %ul\n", len);
	printf("[*] Allocated = %d\n", len);
	for (i = 0, i < len; i++)
		printf("Element %d: %s\n", i, PyList_Type(p[i]));
}
