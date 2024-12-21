use std::rc::Rc;


pub struct LinkedList<T> {
    head: Link<T>,
    pub size: u32,
}

type Link<T> = Option<Rc<Node<T>>>;

struct Node<T> {
    elem: T,
    next: Link<T>,
}
