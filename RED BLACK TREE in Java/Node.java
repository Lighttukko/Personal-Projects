public class Node {
  int key;
  Node left, right;
  boolean isred;
  public int root;

  public Node(int key) {
    this(key, null, null, true);
  }
  public Node(int key, Node left, Node right, boolean isred) {
      this.key = key;
      this.left = left;
      this.right = right;
      this.isred = isred;
  }
  public void accept(Visitor v) {
    v.visitNode(this);
  }

  // public Node delete(int num){
  //   //when it does not exist.
  //   if (!this.find(num)){
  //     return this;
  //   }
  //   //to not waste time, we are not going to find the number each time.
  //   return this.del(num);
  // }

  // public Node del(int num){
  //   if (num == this.key) {
  //     if (this.right == null) return this.left;
  //     if (this.left == null)  return this.right;
  //     Node a = this.left;
  //     while(a.right!=null){
  //       if(a.right.right == null){
  //         break;
  //       }
  //       a = a.right;
  //     }
  //     this.key = a.right.key;
  //     a.right = null;
  //   } else {
  //     if (num < this.key) {
  //       if (this.left != null)
  //         this.left = this.left.delete(num);
  //     } else {
  //       if (this.right != null)
  //         this.right = this.right.delete(num);
  //     }
  //   }
  //   return this;
    // if (num == this.key){ //when we found the deleting node key.
    //   if (this.isred || true){
    //     if(!havechild(this)){//red not without child
    //       return null;
    //     }
    //     else if (this.right != null && this.left != null){//when it has both child.
    //       Node a = this.left;
    //       while(a.right!=null){
    //         if(a.right.right == null){
    //           break;
    //         }
    //         a = a.right;
    //       }
    //       this.key = a.right.key;
    //       a = new Node(a.key, a.left, null, a.isred);
    //     }
    //   }
    //   else{ //black case
    //     return null;
    //   }
    // }
    // else if (num > this.key){ //when it greater than the key.
    //   this.right = this.right.del(num);
    // }
    // else{ //when it less than the key.
    //   this.left = this.left.del(num);
    // }
    // return this;
  // }

  private boolean red(Node n){
    return n != null && n.isred;
  }
  private boolean havechild(Node n){
    if (n == null){return false;}
    return n.left != null || n.right != null;
  }


  public void insert(int num){
    if (num == this.key){
      return;
    }
    else if (num < this.key) {
      if (this.left == null) {
          this.left = new Node(num);
      } else {
          this.left.insert(num);     
      }
    } 
    else if (num > this.key) {
      if (this.right == null) {
        this.right = new Node(num);
      } else {
        this.right.insert(num);
      }
    }
    if (this.key == root){
      this.accept(new Reporter());
      System.out.println("---------after inserted " + num + "-----------");
      this.check(this, num);
      if (this.isred){
        this.isred = false;
        this.accept(new Reporter());
        System.out.println("---------fix red root node!!!-----------");
      }
    }
  }


  public void check(Node original, int num){
    if (num == this.key){
      // System.out.println("hi");
    }
    else if (num > this.key){
      this.right.check(original, num);
      }
    else{
      this.left.check(original, num);
    }
    this.checker(original);
    
  }
  public void checker(Node original){
    if (havechild(this)){
      if (this.left != null && red(this.left)){
        if(red(this.left.left)){
          Node a = new Node(this.key, this.left.right, this.right, false);
          this.key = this.left.key;
          this.isred = true;
          this.left = new Node(this.left.left.key, this.left.left.left, this.left.left.right, false);
          this.right = new Node(a.key, a.left, a.right, false);
          original.accept(new Reporter());
          System.out.println("---------fix double red nodes!!!-----------");
          if (this.right.key == root){
            root = this.key;
          }
        }
        else if(red(this.left.right)){
          Node a = new Node(this.key, this.left.right.right, this.right, false);
          Node b = new Node(this.left.key, this.left.left, this.left.right.left, false);
          this.key = this.left.right.key;
          this.left = new Node(b.key, b.left, b.right, false);
          this.right = new Node(a.key, a.left, a.right, false);
          this.isred = true;
          original.accept(new Reporter());
          System.out.println("---------fix double red nodes!!!-----------");
          if (this.right.key == root){
            root = this.key;
          }
        }
      }
      if (this.right != null && red(this.right)){
        if(red(this.right.left)){
          Node a = new Node(this.key, this.left, this.right.left.left, false);
          Node b = new Node(this.right.key, this.right.left.right, this.right.right, false);
          this.key = this.right.left.key;
          this.left = new Node(a.key, a.left, a.right, false);
          this.right = new Node(b.key, b.left, b.right, false);
          this.isred = true;
          original.accept(new Reporter());
          System.out.println("---------fix double red nodes!!!-----------");
          if (this.left.key == root){
            root = this.key;
          }
        }
        else if(red(this.right.right)){
          Node a = new Node(this.key, this.left, this.right.left, false);
          this.key =this.right.key;
          this.isred = true;
          this.left = new Node(a.key, a.left, a.right, false);
          this.right = new Node(this.right.right.key, this.right.right.left, this.right.right.right, false);
          original.accept(new Reporter());
          System.out.println("--------- fix double red nodes!!!-----------");
          if (this.left.key == root){
            root = this.key;
          }
        }
      }
    }
  }


  // if (havechild(this)){
  //   if (this.left != null && red(this.left)){
  //     if(red(this.left.left)){
  //       //fixer
  //       // this.accept(new Reporter());
  //       //
  //       Node a = new Node(this.key, this.left.right, this.right, false);
  //       this.key = this.left.key;
  //       this.isred = true;
  //       this.left = new Node(this.left.left.key, this.left.left.left, this.left.left.right, false);
  //       this.right = new Node(a.key, a.left, a.right, false);
  //       if (this.right.key == root){
  //         this.isred = false;
  //         root = this.key;
  //       }
  //     }
  //     else if(red(this.left.right)){
  //       Node a = new Node(this.key, this.left.right.right, this.right, false);
  //       Node b = new Node(this.left.key, this.left.left, this.left.right.left, false);
  //       this.key = this.left.right.key;
  //       this.left = new Node(b.key, b.left, b.right, false);
  //       this.right = new Node(a.key, a.left, a.right, false);
  //       this.isred = true;
  //       if (this.right.key == root){
  //         this.isred = false;
  //         root = this.key;
  //       }
  //     }
  //   }
  //   if (this.right != null && red(this.right)){
  //     if(red(this.right.left)){
  //       Node a = new Node(this.key, this.left, this.right.left.left, false);
  //       Node b = new Node(this.right.key, this.right.left.right, this.right.right, false);
  //       this.key = this.right.left.key;
  //       this.left = new Node(a.key, a.left, a.right, false);
  //       this.right = new Node(b.key, b.left, b.right, false);
  //       this.isred = true;
  //       if (this.left.key == root){
  //         this.isred = false;
  //         root = this.key;
  //       }
  //     }
  //     else if(red(this.right.right)){
  //       Node a = new Node(this.key, this.left, this.right.left, false);
  //       this.key =this.right.key;
  //       this.isred = true;
  //       this.left = new Node(a.key, a.left, a.right, false);
  //       this.right = new Node(this.right.right.key, this.right.right.right, this.right.right.left, false);
  //       if (this.left.key == root){
  //         this.isred = false;
  //         root = this.key;
  //       }
  //     }
  //   }
  // }
  // public Node delete(int num){
  //   if (!this.find(num)){
  //       return this;
  //   }
  //   if (this.key == num){
  //     if (this.isred){
  //       if (this.left != null){
  //         if (this.left.right != null){
  //           Node a = this.left;
  //           while (a.right != null){
  //             a = a.right;
  //           }
  //           this.key = a.key;
  //           this.left = new Node(this.left.key, this.left.left, this.left.right, this.left.isred);
  //         }

          
  //       }
  //       else{
  //         return null;
  //       }
  //       }
  //     }
  //     else{//it is black
        
  //     }
  //   }
  //   else if (num > this.key){
  //     this.right.delete(num);
  //   }
  //   else if (num < this.key){
  //     this.left.delete(num);
  //   }
  //   return this;
  // }
      // else if (red(this.right)){

      // }
    // }
    // else if (red(this.right) && this.right != null){
    //   if(red(this.left)){
    //   }
    //   else if (red(this.right)){

    //   }
    // }


  // public void insert(int num) {
  // if (num < this.key) {
  //     if (this.left == null) {
  //         this.left = new Node(num);
  //     } else {
  //         this.left.insert(num);
  //     }
  // } else if (num > this.key) {
  //     if (this.right == null) {
  //         this.right = new Node(num);
  //     } else {
  //         this.right.insert(num);
  //     }
  // }
  // else{

  // }

  // if (havechild(this)){
  //   System.out.println("hi");
  //   if (havechild(this.left)){
  //     if ((red(this.left.left) && red(this.left) || red(this.left.right) && red(this.right)) && red(this.right)){
  //       this.left.isred = !this.left.isred;
  //       this.isred = !this.isred;
  //       this.right.isred = !this.right.isred;
  //     }
  //     else if (!red(this.right)){
  //       if (red(this.left.right) && red(this.left)){
  //         Node a = this.left;
  //         a.right = this.left.right.left;
  //         this.left.right.left = a;
  //         this.left = this.left.right;
  //       }
  //       else if (red(this.left.left) && red(this.left)){
  //           // System.out.println("halo");
  //           // Node a = new Node(this);
  //           // a.left = this.left.right;
  //           // if (this.left.right != null) {
  //           //   this.left.right = new Node(a.key, a.left, a.right, a.isred);
  //           // }
  //           // this.key = this.left.key;
  //           // this.left = this.left.left;
  //           // this.right = this.left.right;
  //           // this.isred = this.left.isred;
  //       }
  //     }

  //   }
  //   if (havechild(this.right)){
  //     if (((red(this.right.left) && red(this.left) || red(this.right.right)) && red(this.right)) && red(this.left)){
  //       this.left.isred = !this.left.isred;
  //       this.isred = !this.isred;
  //       this.right.isred = !this.right.isred;
  //     }
  //     else if (!red(this.left)){
  //       if (red(this.right.left) && red(this.right)){
  //         Node a = this.right;
  //         a.left = this.right.left.right;
  //         this.right.left.right = a;
  //         this.right = this.right.left;
  //       }
  //       else if (red(this.right.right) && red(this.right)){
  //         Node a = this;
  //         a.right = this.right.left;
  //         this.right.left = new Node(a.key, a.left, a.right, a.isred);
  //         this.key = this.right.key;
  //         this.left = this.right.left;
  //         this.right = this.right.right;
  //       }
  //     }
  //   }
  // }
  // if (red(this.left) && red(this.right)){
  //   this.isred = false;
  // }

  // }

 

  public boolean find(int anything) {
    if (anything == this.key)
      return true;
    else if (anything > this.key)
      if (this.right != null)
        return this.right.find(anything);
      else
        return false;
    else if (this.left != null)
      return this.left.find(anything);
    else
      return false;
  }
}

  // public Node delete(int num) {
    // if (num == this.key) {
    //   if (this.right == null) return this.left;
    //   if (this.left == null)  return this.right;
    //   Node a = this.left;
    //   while (a.right != null)
    //     a = a.right;
    //   a.right = this.right;
    //   return this.left;
    // } else {
    //   if (num < this.key) {
    //     if (this.left != null)
    //       this.left = this.left.delete(num);
    //   } else {
    //     if (this.right != null)
    //       this.right = this.right.delete(num);
    //   }
    //   return this;
    // }
  // }