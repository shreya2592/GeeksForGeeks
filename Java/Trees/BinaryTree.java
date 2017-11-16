package tree;

import tree.Node;

public class BinaryTree {

	Node root;
	
	BinaryTree(int key){
		root=new Node(key);
	}
	
	BinaryTree(){
		root=null;
	}
	
	
	public static void main(String args[]){
		BinaryTree tree=new BinaryTree();
		
		tree.root=new Node(1);
		tree.root.left=new Node(2);
		tree.root.right=new Node(3);
		
		
	}
}
