#include "lists.h"

void set_newnode(listint_t **previous, listint_t **newnode);

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
		return (*head);
	}
	if (*head == NULL)
	{
		(*head) = newnode;
		return (*head);
	}
	if ((*head)->n > number)
	{
		set_newnode(head, &newnode);
		return (*head);
	}
	turtle = (*head);
	rabbit = (*head);
	while (rabbit->next != NULL && rabbit->next->next != NULL)
	{
		rabbit = rabbit->next->next;
		if (rabbit->n < number)
			turtle = rabbit;
		else if (turtle->next->n < number)
		{
			set_newnode(&turtle->next, &newnode);
			return (newnode);
		}
		else if (turtle->n < number)
		{
			set_newnode(&turtle, &newnode);
			return (newnode);
		}
	}
	if (rabbit->next == NULL)
	{
		rabbit->next = newnode;
		return (newnode);
	}
	if (rabbit->next->n > number)
	{
		rabbit->next->next = newnode;
		return (newnode);
	}
	set_newnode(&rabbit, &newnode);
	return (newnode);
}

/**
 * set_newnode - function to set value of newnode
 * @previous: input pointer to previous node pointer
 * @newnode: input pointer to newnode pointer
 */
void set_newnode(listint_t **previous, listint_t **newnode)
{
	(*newnode)->next = (*previous)->next;
	(*previous)->next = (*newnode);
}
