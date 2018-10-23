// binary tree three traversal method: preorder, inorder and postorder
import java.util.Stack;

public class PreInPosTraversal {
    public static class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int data) {
            this.value = data;
        }
    }

    // preorder recursive
    public static void preOrderRecur(Node head) {
        if (head == null) {
            return;
        }
        System.out.print(head.value + " ");
        preOrderRecur(head.left);
        preOrderRecur(head.right);
    }

    // inorder recursive
    public static void inOrderRecur(Node head) {
        if (head == null) {
            return;
        }
        inOrderRecur(head.left);
        System.out.print(head.value + " ");
        inOrderRecur(head.right);
    }

    // postorder recursive
    public static void posOrderRecur(Node head){
        if (head == null) {
            return;
        }
        posOrderRecur(head.left);
        posOrderRecur(head.right);
        System.out.print(head.value + " ");
    }

    // preorder unrecursive
    public static void preOrderUnRecur(Node head) {
        System.out.print("Pre-order: ");
        if (head != null) {
            Stack<Node> stack = new Stack<Node>();
            stack.push(head);
            while (!stack.isEmpty()) {
                head = stack.pop();
                System.out.print(head.value + " ");
                if (head.right != null) {
                    stack.push(head.right);
                }
                if (head.left != null) {
                    stack.push(head.left);
                }
            }
        }
        System.out.println();
        
    }

    // inorder unrecursive
    public static void inOrderUnRecur(Node head) {
        System.out.print("In-order: ");
        if (head != null) {
            Stack<Node> stack = new Stack<Node>();
            while (!stack.isEmpty() || head != null) {
                if (head != null) {
                    stack.push(head);
                    head = head.left;
                } else {
                    head = stack.pop();
                    System.out.print(head.value + " ");
                    head = head.right;
                }
            }
        }
        System.out.println();
    }

    // postorder unrecursive
    public static void posOrderUnRecur(Node head) {
        System.out.print("Post-order: ");
        if (head != null) {
            Stack<Node> stackData = new Stack<Node>();
            Stack<Node> stackTraversal = new Stack<Node>();
            stackTraversal.push(head);
            while (!stackTraversal.isEmpty()) {
                head = stackTraversal.pop();
                stackData.push(head);
                if (head.left != null) {
                    stackTraversal.push(head.left);
                }
                if (head.right != null) {
                    stackTraversal.push(head.right);
                }
            }
            while (!stackData.isEmpty()) {
                System.out.print(stackData.pop().value + " ");
            }
        }
        System.out.println();
    }

    
    public static void main(String[] args) {
		Node head = new Node(5);
		head.left = new Node(3);
		head.right = new Node(8);
		head.left.left = new Node(2);
		head.left.right = new Node(4);
		head.left.left.left = new Node(1);
		head.right.left = new Node(7);
		head.right.left.left = new Node(6);
		head.right.right = new Node(10);
		head.right.right.left = new Node(9);
		head.right.right.right = new Node(11);

		// recursive
		System.out.println("==============recursive==============");
		System.out.print("pre-order: ");
		preOrderRecur(head);
		System.out.println();
		System.out.print("in-order: ");
		inOrderRecur(head);
		System.out.println();
		System.out.print("pos-order: ");
		posOrderRecur(head);
        System.out.println();    
        
        // unrecursive
        System.out.println("==============unrecursive==============");
        preOrderUnRecur(head);
        inOrderUnRecur(head);
        posOrderUnRecur(head);
    }
}