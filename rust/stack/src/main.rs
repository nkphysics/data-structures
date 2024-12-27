// Reference: https://rust-unofficial.github.io/too-many-lists/third.html

use std::rc::Rc;

pub struct Stack<T> {
    head: Link<T>,
}

type Link<T> = Option<Rc<Node<T>>>;

struct Node<T> {
    elem: T,
    next: Link<T>,
}

impl<T> Stack<T> {
    pub fn new() -> Self {
        Stack { head: None }
    }

    pub fn push(&self, elem: T) -> Stack<T> {
        Stack { head: Some(Rc::new(Node {
            elem: elem,
            next: self.head.clone(),
        }))}
    }

    pub fn pop(&self) -> Stack<T> {
        Stack { head: self.head.as_ref().and_then(|node| node.next.clone()) }
    }

    pub fn peek(&self) -> Option<&T> {
        self.head.as_ref().map(|node| &node.elem)
    }
}


#[cfg(test)]
mod test {
    use super::Stack;

    #[test]
    fn basics() {
        let stack = Stack::new();
        assert_eq!(stack.peek(), None);

        let stack = stack.push("cherry").push("bannana").push("apple");
        assert_eq!(stack.peek(), Some(&"apple"));

        let stack = stack.pop();
        assert_eq!(stack.peek(), Some(&"bannana"));

        let stack = stack.pop();
        assert_eq!(stack.peek(), Some(&"cherry"));

        let stack = stack.pop();
        assert_eq!(stack.peek(), None);

        let stack = stack.pop();
        assert_eq!(stack.peek(), None);
    }
}


fn main() {
    let stack = Stack::new();
    let stack = stack.push("cherry").push("bannana").push("apple");
    let fruit = stack.peek();
    println!("{:?}", fruit.unwrap());
    let stack = stack.pop();
    let fruit = stack.peek();
    println!("{:?}", fruit.unwrap());
    let stack = stack.pop();
    let fruit = stack.peek();
    println!("{:?}", fruit.unwrap());
}
