#include "tree.h"

int Tree::counter = 1;

Tree::Tree()
{
    root = nullptr;
}

Tree::~Tree()
{
    freeTree(root);
}

void Tree::print()
{
    printTree(root);
}

void Tree::printFile(QTextStream &stream)
{
    printTreeFile(root, stream);
}

void Tree::printTree(Node *root)
{
    if (root == nullptr) {
        return;
    }

    std::cout << root->number << " ";
    printTree(root->left);
    printTree(root->right);
}

void Tree::writeToFile() {
    std::string name = "../files/txt_files/graph" + std::to_string(Tree::counter) + ".txt";
    QString filename = name.c_str();
    QFile file(filename);
    Tree::counter++;

    if ( file.open(QIODevice::ReadWrite | QIODevice::Truncate) ){
        QTextStream stream( &file );

        printFile(stream);

        file.close();
    }
}

void Tree::printTreeFile(Node *root, QTextStream &stream)
{
    if (root == nullptr)
        return;

    stream << root->number << " ";
    if (root->left == nullptr && root->right == nullptr) {
        stream << endl;
        return;
    }
    else if (root->left != nullptr && root->right == nullptr) {
        stream << root->left->number << endl;
    }
    else if (root->left == nullptr && root->right != nullptr) {
        stream << root->right->number << endl;
    }
    else {
        stream << root->left->number << " " << root->right->number << endl;
    }

    printTreeFile(root->left, stream);
    printTreeFile(root->right, stream);
}


void Tree::addNumber(int number)
{
    addNode(&root, number);
}

void Tree::addNode(Node **root, int number)
{
    if (*root == nullptr) {
        *root = new Node;
        (*root)->left = nullptr;
        (*root)->right = nullptr;
        (*root)->number = number;
        return ;
    }

    if (number < (*root)->number) {
        addNode(&(*root)->left, number);
    }
    else {
        addNode(&(*root)->right, number);
    }
}

void Tree::freeTree(Node *root)
{
    if (root != nullptr) {
        freeTree(root->left);
        freeTree(root->right);
        delete root;
    }
}

void Tree::rotateRightOnce(Node **node)
{
    if ((*node)->left) {
        Node *tmp = (*node)->right;
        Node *nodeTmp = (*node);
        Node *tmpRight = (*node)->left->right;
        (*node) = (*node)->left;
        (*node)->right = nodeTmp;
        nodeTmp->right = tmp;
        nodeTmp->left = tmpRight;
    }
}

void Tree::rotateRight()
{
    while (root->left) {
        rotateRightOnce(&root);
        writeToFile();
    }
    Node *rootPom1 = root;
    Node *rootPom2 = root->right;

    while (rootPom1->right) {
        while (rootPom2 && rootPom2->left) {
            rotateRightOnce(&rootPom2);
        }
        rootPom1->right = rootPom2;
        rootPom1 = rootPom1->right;
        if (rootPom2)
            rootPom2 = rootPom2->right;
        writeToFile();
    }
}

void Tree::rotateLeft(Tree &t2)
{
    Node *node2 = t2.root;
    rotateLeftOnce(&root, node2);
}

void Tree::rotateLeftOnce(Node **root, Node *root2)
{
    if (!root2)
        return ;

    if (root2->left) {
        Node *pom = findNode(*root, root2->number);
        Node *pom2 = findLeftSubTree(*root, root2->number);
        *root = pom;
        (*root)->left = pom2;
        writeToFile();
    }
    rotateLeftOnce(&(*root)->left, root2->left);
    rotateLeftOnce(&(*root)->right, root2->right);
}

Node *Tree::findNode(Node *root, int number)
{
    while (root) {
        if (root->number == number)
            return root;
        root = root->right;
    }

    return nullptr;
}

Node *Tree::findLeftSubTree(Node *root, int number)
{
    Node *pom = root;
    while (root->right) {
        if (root->right->number == number) {
            root->right = nullptr;
            break;
        }
        root = root->right;
    }
    return pom;
}

