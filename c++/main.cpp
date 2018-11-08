#include <iostream>
#include "tree.h"

using namespace std;

int jednaka (Node *g1, Node *g2)
{
  if (!g1 && !g2)
    return 1;

  if ((!g1 && g2) || (g1 && !g2))
    return 0;

  if (g1->number != g2->number)
    return 0;
  else
    return jednaka(g1->left, g2->left) && jednaka(g1->right, g2->right);
}

int main()
{
    Tree *t = new Tree();
    Tree *t2 = new Tree();

    t->addNumber(10);
    t->addNumber(7);
    t->addNumber(5);
    t->addNumber(4);
    t->addNumber(9);
    t->addNumber(15);
    t->addNumber(13);
    t->addNumber(17);
    t->addNumber(6);

    t2->addNumber(7);
    t2->addNumber(9);
    t2->addNumber(5);
    t2->addNumber(4);
    t2->addNumber(10);
    t2->addNumber(15);
    t2->addNumber(13);
    t2->addNumber(17);
    t2->addNumber(6);

//    t->addNumber(2);
//    t->addNumber(10);
//    t->addNumber(5);
//    t->addNumber(3);
//    t->addNumber(7);
//    t->addNumber(9);

//    t2->addNumber(7);
//    t2->addNumber(9);
//    t2->addNumber(3);
//    t2->addNumber(5);
//    t2->addNumber(10);
//    t2->addNumber(2);

//    t->addNumber(1);
//    t->addNumber(4);

//    t2->addNumber(4);
//    t2->addNumber(1);

    t->writeToFile();
    t2->writeToFile();


    t->rotateRight();
    t->rotateLeft(*t2);

    cout << jednaka(t->getRoot(), t2->getRoot()) << endl;

    delete t;
    delete t2;

    string command = "python draw_graph.py " + to_string(Tree::counter);
    system(command.c_str());
    return 0;
}

