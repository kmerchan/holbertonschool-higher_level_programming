#include "lists.h"

/**
 * check_cycle - function to check if singly linked list has a cycle
 * @list: head pointer to singly linked list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *holder = list;
	listint_t *mover = holder;
	int counter = 0, i = 0;

	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		list = list->next;
		counter++;
		mover = holder;
		for (i = 0; i < counter; i++)
		{
			if (list == mover)
				return (1);
		}
	}
	return (0);
}
