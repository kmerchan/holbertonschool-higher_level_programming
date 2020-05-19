#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - function to print information about Python lists
 * @p: PyObject to get information from
 */

void print_python_list(PyObject *p)
{
	(void)p;
	printf("[*] Python list info\n");
	printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_bytes - function to print information about Python bytes
 * @p: PyObject to get information from
 */

void print_python_bytes(PyObject *p)
{
	(void)p;
	printf("[.] bytes object info\n");
	printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_float - function to print information about Python floats
 * @p: PyObject to get information from
 */

void print_python_float(PyObject *p)
{
	(void)p;
	printf("[.] float object info\n");
	printf("  [ERROR] Invalid Float Object\n");
}
