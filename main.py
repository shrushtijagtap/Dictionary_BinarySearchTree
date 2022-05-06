#include <iostream>
#include<string.h>
using namespace std;

struct node
{
    char word[10];
    char meaning[10];
    node *left,*right;
};
class dict
{
    node *root,*
    curr;
    public:
    void create()
    {
        char ans;

       while(1)
       {
           node *temp=new node();
           cout<<"enter word & meaning"<<endl;
           cin>>temp->word>>temp->meaning;
                if(root==NULL)
                   {
                    root=temp;
                    root->right=NULL;
                    root->left=NULL;
                    curr=root;
                   }
                else
                   {
                       curr=root;
                       while(curr!=NULL)
                       {
                       if(strcmp(curr->word,temp->word)<0)
                       {
                           if(curr->left==NULL)
                           {
                               curr->left=temp;
                               break;
                           }
                           else
                            curr=curr->left;
                       }
                       else if(strcmp(curr->word,temp->word)>0)
                       {
                           if(curr->right==NULL)
                           {
                               curr->right=temp;
                               break;
                           }
                           else
                            curr=curr->right;
                       }
                       else
                        break;
                   }
                   }
       cout<<"more nodes ? y or n"<<endl;
       cin>>ans;
       if(ans=='n')
        break;
       }
    }
    void display()
    {
        cout<<"ascending : ";
        curr=root;
        asc(curr);
        cout<<"descending : ";
        curr=root;
        des(curr);
    }
    void asc(node *t)
    {
        if(t->left!=NULL)
            asc(t->left);
        cout<<t->word<<"\t"<<t->meaning;
        if(t->right!=NULL)
            asc(t->right);
    }
    void des(node *t)
    {
        if(t->right!=NULL)
            des(t->right);
        cout<<t->word<<"\t"<<t->meaning;
        if(t->left!=NULL)
            des(t->left);
    }
    void update()
    {
        curr=root;
        char w[10],m[10];
        cout<<"enter word to be up & meaning"<<endl;
        cin>>w>>m;
        while(curr!=NULL)
        {
            if(strcmp(w,curr->word)==0)
            {
                strcpy(curr->meaning,m);
                return;
            }
            if(strcmp(w,curr->word)<0)
                curr=curr->left;
            if(strcmp(w,curr->word)>0)
                curr=curr->right;
        }
    }
    void delete()
    {
        char w[10];
        cout<<"enter word to b  deleted"<<endl;
        cin>>w;
        curr=root;
        node*p=new node();
        p=root;
        while(curr!=NULL)
        {
            if(strcmp(w,curr->word)==0)
            {
                if(curr->left==NULL && curr->right==NULL)
                {
                    if(curr==p->right)
                        p->right=NULL;
                    if(curr==p->left)
                        p->left=NULL;
                    delete curr;
                }
                if(curr->left!=NULL && curr->right!=NULL)
                {
                   node *t=new node();
                   p=curr;
                   t=curr->right;
                   while(t->left!=NULL)
                    t=t->left;

                   if(p)
                }
                if(curr->left==NULL && curr->right!=NULL )
                {
                     if(curr=p->left)
                        p->left=curr->right;
                    if(curr=p->right)
                        p->right=curr->right;
                    delete curr;
                }
                if(curr->left!=NULL && curr->right==NULL)
                {
                     if(curr=p->left)
                        p->left=curr->left;
                    if(curr=p->right)
                        p->right=curr->left;
                    delete curr;
                }
            }
            if(strcmp(w,curr->word)<0)
               {
                p=curr;
                curr=curr->left;
               }
            if(strcmp(w,curr->word)>0)
               {
                  p=curr;
                curr=curr->right;
               }
        }
    }
};
int main()
{
    dict d;
    d.create();
    d.display();
    return 0;
}
