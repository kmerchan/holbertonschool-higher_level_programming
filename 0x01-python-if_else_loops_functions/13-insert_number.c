#include "lists.h"

/**
 * insert_node - function to insert new node in sorted linked list
 * @head: input pointer to head pointer of singly linked list
 * @number: input number to sort and insert into list as new node
 * Return: pointer to newly added node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t)), *turtle, *rabbit;

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if (head == NULL)
	{
		head = &newnode;
		return (newnode);
	}
	if (*head == NULL)
	{
		(*head) = newnode;
		return (newnode);
	}
	if ((*head)->n >= number)
	{
		newnode->next = (*head);
		(*head) = newnode;
		return (newnode);
	}
	turtle = (*head);
	rabbit = (*head);
	while (rabbit->next != NULL && rabbit->next->next != NULL)
	{
		rabbit = rabbit->next->next;
		if (rabbit->n < number)
			turtle = rabbit;
		else if (turtle->next->n <= number)
		{
			newnode->next = turtle->next->next;
			turtle->next->next = newnode;
			return (newnode);
		}
		else if (turtle->n <= number)
		{
			newnode->next = turtle->next;
			turtle->next = newnode;
			return (newnode);
		}
	}
	if (rabbit->next == NULL)
	{
		rabbit->next = newnode;
		return (newnode);
	}
	if (rabbit->next->n <= number)
	{
		rabbit->next->next = newnode;
		return (newnode);
	}
	newnode->next = rabbit->next;
	rabbit->next = newnode;
	return (newnode);
}
