public class CompleteTreeNodeNumber {

    public static class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int data) {
            this.value = data;
        }
    }

    public static int nodeNum(Node head) {
        if (head == null) {
            return 0;
        }
        return bs(head, 1, mostLeftLevel(head, 1));
    }

    // compute the number of node
    // level: level of the current node
    // h: height of the tree with current node root
    public static int bs(Node node, int level, int h) {
        if (level == h) {
            return 1;
        }
        // if the height right child equals the height of the whole tree 
        if (mostLeftLevel(node.right, level + 1) == h) {
            // left child is complete
            // recursive on right child
            return (1 << (h - level)) + bs(node.right, level + 1, h);
        } else {
            // right child is complete (height = h - 1)
            // recursive on left child
            return (1 << (h - 1 - level)) + bs(node.left, level + 1, h);
        }
    }
    
    // compute the height of the tree
    public static int mostLeftLevel(Node node, int level) {
        while (node != null) {
            level++;
            node = node.left;
        }
        return level - 1;
    }

    public static void main(String[] args) {
		Node head = new Node(1);
		head.left = new Node(2);
		head.right = new Node(3);
		head.left.left = new Node(4);
		head.left.right = new Node(5);
		head.right.left = new Node(6);
		System.out.println(nodeNum(head));        
    }
}