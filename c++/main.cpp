#include <iostream>
#include <QTextStream>
#include <QIODevice>
#include <QFile>
#include <QString>
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
    QString filename1 = "test_pre.txt";
    QString filename4 = "test_pre_drugo.txt";
    QString filename2 = "test_posle.txt";
    QString filename3 = "test_final.txt";
    QFile file1(filename1);
    QFile file2(filename2);
    QFile file3(filename3);
    QFile file4(filename4);

    if ( file1.open(QIODevice::ReadWrite) && file2.open(QIODevice::ReadWrite)
         && file3.open(QIODevice::ReadWrite) && file4.open(QIODevice::ReadWrite) )
    {
        QTextStream stream1( &file1 );
        QTextStream stream2( &file2 );
        QTextStream stream3( &file3 );
        QTextStream stream4( &file4 );

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

        t->printFile(stream1);
        t->rotateRight();

        t->printFile(stream2);

        t->rotateLeft(*t2);
//        t->print();

//        std::cout << std::endl;

        t->printFile(stream3);
        t2->printFile(stream4);
//        t2->print();
//        std::cout << std::endl;

        cout << jednaka(t->getRoot(), t2->getRoot()) << endl;

        delete t;
        delete t2;
        file1.close();
        file2.close();
        file3.close();
        file4.close();



        system("python draw_graph.py");
        return 0;
    }

    return 0;
}

