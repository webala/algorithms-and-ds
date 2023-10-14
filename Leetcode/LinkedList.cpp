#include <iostream>
using namespace std;


class Node {
   public:
      int Value;
      Node* Next;
};

void printList(Node* n) {
   // bool print = true;
   // Node* currentNode = head;
   // cout << "Start of the list \n";
   // while (print)
   // {
   //    /* code */
   //    cout << currentNode->Value << endl;
   //    if (currentNode->Next) {
   //       currentNode = currentNode->Next;
   //    } else {
   //       cout << "end of list \n";
   //       print = false;
   //    }
   // }

   while (n!=NULL)
   {
      /* code */
      cout << n->Value << endl;
      n = n->Next;
   }
   
   
}

int main() {

   Node* head = new Node();
   Node* second = new Node();
   Node* third = new Node();

   // This is how you access members of a class if you are using pointers;
   head->Value = 1;
   head->Next = second;

   second->Value = 2;
   second->Next = third;
   third->Value = 3;
   third->Next = NULL;

   printList(head);
   return 0;
}