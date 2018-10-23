import java.util.Stack;

public class GetMinStack {
    private Stack<Integer> stackData;
    private Stack<Integer> stackMin;

    public GetMinStack() {
        this.stackData = new Stack<Integer>();
        this.stackMin = new Stack<Integer>();
    }

    public void push(int obj) {
        this.stackData.push(obj);
        if (this.stackMin.isEmpty()) {
            this.stackMin.push(obj);
        } else {
            int minnum = Math.min(obj, this.stackMin.peek());
            this.stackMin.push(minnum);
        }
    }

    public Integer pop() {
        if (this.stackData.isEmpty()) {
            throw new RuntimeException("Your Stack is empty!");
        }
        int value = this.stackData.pop();
        this.stackMin.pop();
        return value;
    }

    public Integer getMin() {
        if (this.stackMin.isEmpty()) {
            throw new RuntimeException("Your stack is empty!");
        }
        return this.stackMin.peek();
    }

    public static void main(String[] args) {
        GetMinStack mystack = new GetMinStack();
        mystack.push(6);
        System.out.println("Min: " + mystack.getMin());
        mystack.push(7);
        System.out.println("Min: " + mystack.getMin());
        mystack.push(4);
        System.out.println("Min: " + mystack.getMin());
        mystack.push(2);
        System.out.println("Min: " + mystack.getMin());
        System.out.println("pop: " + mystack.pop());
        System.out.println("Min: " + mystack.getMin());
        System.out.println("pop: " + mystack.pop());
        System.out.println("Min: " + mystack.getMin());
    }
}