#ifndef TREE_H
#define TREE_H

#include <iostream>
#include <QTextStream>

struct Node {
    int number;
    struct Node *left;
    struct Node *right;
};

class Tree
{
public:
    Tree();
    ~Tree();
    void printTree(Node *root);
    void printTreeFile(Node *root, QTextStream &stream);
    void addNumber(int number);
    void print();
    void printFile(QTextStream &stream);
    void addNode(Node **root, int number);
    Node *getRoot() { return root; }
    void freeTree(Node *root);
    void rotateOnce(Node **node);
    void rotateRight();
    void rotateLeft(Tree &t2);
    void rotateLeftOnce(Node **root, Node *root2);
    Node *findNode(Node *root, int number);
    Node *findLeftSubTree(Node *root, int number);

private:
    Node *root;
};

#endif // TREE_H

