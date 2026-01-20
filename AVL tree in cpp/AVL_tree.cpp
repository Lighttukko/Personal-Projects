#include <iostream>
class Node{
    public:
        int data;
        int height;
        Node *left;
        Node *right;
        Node(int data){
            this->data = data;
            this->height = 1;
            this->left = nullptr;
            this->right = nullptr;
            
        }
};

bool search(Node *node, int num){
    if (node == nullptr){
        return false;        
    } else if (node->data == num){
        return true;
    } else if(node->data > num){
        return search(node->left, num);
    } else{
        return search(node->right, num);
    }
}


int max(int num1, int num2){
    return (num1 > num2) ? num1 : num2;
}

int height(Node *node){
    if (node == nullptr){
        return 0;
    }
    return node->height;
}
int getbalance(Node *node){
    if (node == nullptr){
        return 0;
    }
    return height(node->left) - height(node->right);
}

Node* right_rotate(Node *node){
    Node *ptr = node->left;
    node->left = node->left->right;
    ptr->right = node;
    node->height = 1 + max(height(node->left), height(node->right));
    ptr->height = 1 + max(height(ptr->left), height(ptr->right));
    return ptr;
}

Node* left_rotate(Node *node){
    Node *ptr = node->right;
    node->right = node->right->left;
    ptr->left = node;
    node->height = 1 + max(height(node->left), height(node->right));
    ptr->height = 1 + max(height(ptr->left), height(ptr->right));
    return ptr;
}

Node* minvalue(Node *node){
    if (node == nullptr){
        return node;
    }
    while (node->left!=nullptr){
        node = node->left;
    }
    return node;
}


Node* insert(Node *node, int num){
    if (node == nullptr){
        return new Node(num);
    } else if (num > node->data){
        node->right = insert(node->right, num);
    } else if (num < node->data){
        node->left = insert(node->left, num);
    } else{
        return node;
    }
    node->height = 1 + max(height(node->left), height(node->right));
    int balance = getbalance(node);
    if (balance > 1 && num < node->left->data){
        return right_rotate(node);
    }
    if (balance < -1 && num > node->right->data){
        return left_rotate(node);
    }
    if (balance > 1 && num > node->left->data){
        node->left = left_rotate(node->left);
        return right_rotate(node);
    }
    if (balance < -1 && num < node->right->data){
        node->right = right_rotate(node->right);
        return left_rotate(node);
    }
    return node;
}

Node* remove(Node *node, int num){
    if (node == nullptr){
        return node;
    }
    if (num < node->data){
        node->left = remove(node->left, num);
    }
    else if (num > node->data){
        node->right = remove(node->right, num);
    }
    else{
        if (node->left == nullptr || node->right == nullptr){
            Node *temp = (node->left!=nullptr) ? node->left : node->right;
            if (temp == nullptr){
                temp = node;
                node = nullptr;
            } else{
                *node = *temp;
            }
            // delete temp;
        }else{
            Node *temp = minvalue(node->right);
            node->data = temp->data;
            node->right = remove(node->right, temp->data);
        }
    }
    if (node == nullptr){
        return nullptr;
    }
    node->height = 1 + max(height(node->left), height(node->right));
    int balance = getbalance(node);
    if (balance > 1 && getbalance(node->left) > -1){
        return right_rotate(node);
    }
    if (balance < -1 && getbalance(node->right) < 1){
        return left_rotate(node);
    }
    if (balance > 1 && getbalance(node->left) < 0){
        node->left = left_rotate(node->left);
        return right_rotate(node);
    }
    if (balance < -1 && getbalance(node->right) > 0){
        node->right = right_rotate(node->right);
        return left_rotate(node);
    }
    return node;
}

void in_order_traversal(Node *node){
    if (node == nullptr){
        return;
    }
    in_order_traversal(node->left);
    std::cout << node->data << std::endl;
    in_order_traversal(node->right);
}

void pre_order_traversal(Node *node){
    if (node == nullptr){
        return;
    }
    std::cout << node->data <<std::endl;
    pre_order_traversal(node->left);
    pre_order_traversal(node->right);
}

void post_order_traversal(Node *node){
    if (node == nullptr){
        return;
    }
    post_order_traversal(node->left);
    post_order_traversal(node->right);
    std::cout << node->data << std::endl;
}

int main(){
    Node *root = nullptr;
    int letters[] = {5, 4, 3, 6, 7, 9, 8};
    int n = sizeof(letters) / sizeof(letters[0]);
    for (int i = 0; i < n; i++) {
        root = insert(root, letters[i]);
    }

    std::cout << root->data << "r  " << height(root) << ";";
    std::cout << root->left->data << "rl  " << height(root->left) << ";";
    std::cout << root->right->data << "rr  " << height(root->right) << ";";
    std::cout << root->left->left->data << "rll  " << height(root->left->left) << ";";
    std::cout << root->left->right->data << "rlr  " << height(root->left->right) << ";";
    std::cout << root->right->left->data << "rrl  " << height(root->right->left) << ";";
    std::cout << root->right->right->data << "rrr  " << height(root->right->right) << ";\n";

    root = remove(root, 4);
    root = remove(root, 3);
    root = remove(root, 5);

    std::cout << root->data << "r  " << height(root) << ";";
    std::cout << root->left->data << "rl  " << height(root->left) << ";";
    std::cout << root->right->data << "rr  " << height(root->right) << ";";
    std::cout << root->left->right->data << "rlr  " << height(root->left->right) << ";";
    // std::cout << root->right->right->data << "rrr  " << height(root->right->right) << ";";
    // std::cout << root->right->left->data << "rrl  " << height(root->right->left) << ";";

    // in_order_traversal(root);
    return 0;
}