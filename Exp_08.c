#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;
} Node;

Node *createNode(int data)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

Node *insertNode(Node *head, int data)
{
    Node *newNode = createNode(data);
    if (head == NULL)
    {
        head = newNode;
    }
    else
    {
        Node *temp = head;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    return head;
}

int getNodeValue(Node *head, int position)
{
    if (head == NULL)
    {
        printf("Error: Linked list is empty.\n");
        return -1;
    }

    Node *temp = head;
    int count = 1;
    while (temp != NULL && count != position)
    {
        temp = temp->next;
        count++;
    }

    if (temp == NULL)
    {
        printf("Error: Position out of range.\n");
        return -1;
    }

    return temp->data;
}

void freeLinkedList(Node *head)
{
    Node *temp;
    while (head != NULL)
    {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main()
{
    Node *head = NULL;
    int n, data;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter the elements:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data);
        head = insertNode(head, data);
    }

    int position;
    printf("Enter the position of the node to retrieve: ");
    scanf("%d", &position);

    int nodeValue = getNodeValue(head, position);
    if (nodeValue != -1)
    {
        printf("Value of the node at position %d: %d\n", position, nodeValue);
    }

    freeLinkedList(head);

    return 0;
}
