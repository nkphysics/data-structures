// Reference: https://rust-unofficial.github.io/too-many-lists/third.html
// RC reference: https://doc.rust-lang.org/rust-by-example/std/rc.html

use std::rc::Rc;
// Reference counting pointer (RC = reference counted)

pub struct Stack<T> {
    head: Link<T>,
    size: u32,
}

type Link<T> = Option<Rc<Node<T>>>;

struct Node<T> {
    elem: T,
    next: Link<T>,
}

impl<T> Stack<T> {
    pub fn new() -> Self {
        Stack { head: None,
                size: 0,
            }
    }

    pub fn push(&self, elem: T) -> Stack<T> {
        // 0(1) linear time
        Stack { head: Some(Rc::new(Node {
            elem: elem,
            next: self.head.clone(),
            })),
            size: self.size + 1
        }
    }

    pub fn pop(&self) -> Stack<T> {
        // 0(1) linear time
        if self.size > 0 {
            Stack { head: self.head.as_ref().and_then(|node| node.next.clone()),
                    size: self.size - 1 }
        } else {
            Stack { head: self.head.as_ref().and_then(|node| node.next.clone()),
                    size: 0 }
        }
    }

    pub fn peek(&self) -> Option<&T> {
        // 0(1) linear time
        self.head.as_ref().map(|node| &node.elem)
    }
}

impl<T> Drop for Stack<T> {
    // Destructor for the Stack
    // Reference on destructors: https://doc.rust-lang.org/stable/reference/destructors.html
    fn drop(&mut self) {
        let mut head = self.head.take();
        while let Some(node) = head {
            if let Ok(mut node) = Rc::try_unwrap(node) {
                head = node.next.take();
            } else {
                break;
            }
        }
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
        assert_eq!(stack.size, 3);

        let stack = stack.pop();
        assert_eq!(stack.peek(), Some(&"bannana"));
        assert_eq!(stack.size, 2);

        let stack = stack.pop();
        assert_eq!(stack.peek(), Some(&"cherry"));
        assert_eq!(stack.size, 1);

        let stack = stack.pop();
        assert_eq!(stack.peek(), None);
        assert_eq!(stack.size, 0);

        let stack = stack.pop();
        assert_eq!(stack.peek(), None);
        assert_eq!(stack.size, 0);
    }
}


fn main() {
    let stack = Stack::new();
    let stack = stack.push("cherry").push("bannana").push("apple");
    let fruit = stack.peek();
    println!("{1}: {0}", fruit.unwrap(), stack.size);
    let stack = stack.pop();
    let fruit = stack.peek();
    println!("{1}: {0}", fruit.unwrap(), stack.size);
    let stack = stack.pop();
    let fruit = stack.peek();
    println!("{1}: {0}", fruit.unwrap(), stack.size);
}
