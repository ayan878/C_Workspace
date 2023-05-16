#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};
struct Node *Head = (struct Node *)malloc(sizeof(struct Node));
Head.data = 50;
Head.next = NULL;
struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
temp.data=60;
temp=NULL;
Head.link=temp;
temp.link=NULL;

