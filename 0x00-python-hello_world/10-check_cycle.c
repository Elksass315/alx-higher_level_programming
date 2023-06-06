#include "lists.h"

/**
 * check_cycle - checks if a linked list with cycle
 * @l: linked list
 *
 * Return: 1 if there is cycle, 0 if no cycle
 */
int check_cycle(listint_t *l)
{
	listint_t *slow = l;
	listint_t *fast = l;

	if (!l)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

