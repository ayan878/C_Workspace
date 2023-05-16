#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node
{
    int data;
    struct Node *next;
};

// Function to create a new node
struct Node *createNode(int data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to create a singly linked list
struct Node *createLinkedList(int *arr, int size)
{
    if (size == 0)
    {
        return NULL;
    }

    struct Node *head = createNode(arr[0]);
    struct Node *current = head;

    for (int i = 1; i < size; i++)
    {
        struct Node *newNode = createNode(arr[i]);
        current->next = newNode;
        current = current->next;
    }

    return head;
}

// Function to display the linked list
void displayLinkedList(struct Node *head)
{
    struct Node *current = head;

    while (current != NULL)
    {
        printf("%d ", current->data);
        current = current->next;
    }

    printf("\n");
}

// Test the functions
int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    struct Node *head = createLinkedList(arr, size);

    printf("Linked List: ");
    displayLinkedList(head);

    return 0;
}