import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class StackAndQueueConvert {
    public static class TwoStackQueue {
        private Stack<Integer> stackPush;
        private Stack<Integer> stackPop;

        public TwoStackQueue() {
            stackPush = new Stack<Integer>();
            stackPop = new Stack<Integer>();
        }

        public void push(int obj) {
            stackPush.push(obj);
        }

        public Integer poll() {
            if (stackPop.isEmpty() && stackPush.isEmpty()) {
                throw new RuntimeException("Queue is empty!");
            } else if (stackPop.isEmpty()) {
                while (!stackPush.isEmpty()) {
                    stackPop.push(stackPush.pop());
                }
            }
            return stackPop.pop();
        }

        public int peek() {
            if (stackPop.isEmpty() && stackPush.isEmpty()) {
                throw new RuntimeException("Queue is empty!");
            } else if (stackPop.isEmpty()) {
                while (!stackPush.isEmpty()) {
                    stackPop.push(stackPush.pop());
                }
            }
            return stackPop.peek();
        }
    }

    public static class TwoQueueStack {
        private Queue<Integer> queue;
        private Queue<Integer> help;

        public TwoQueueStack() {
            queue = new LinkedList<Integer>();
            help = new LinkedList<Integer>();
        }

        public void push(int obj) {
            queue.add(obj);
        }

        public int peek() {
            if (queue.isEmpty()) {
                throw new RuntimeException("Stack is empty!");
            }
            while (queue.size() != 1) {
                help.add(queue.poll());
            }
            int res = queue.poll();
            help.add(res);
            swap();
            return res;
        }

        public int pop() {
            if (queue.isEmpty()) {
                throw new RuntimeException("Stack is empty!");
            }
            while (queue.size > 1) {
                help.add(queue.poll());
            }
            int value = queue.poll();
            swap();
            return value;
        }
        
        private void swap() {
            Queue<Integer> tmp = help;
            help = queue;
            queue = tmp;
        }
    }
}