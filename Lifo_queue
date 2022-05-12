#include <iostream>

using namespace std;

class Lifo {
private:
	struct lifo_node
	{
		//value of an specific elemet
		int data; 
		//indicator that shows adress of next data/element memory adress
		struct lifo_node *next;
	}head;
public:
	void put(int data_value);
	Lifo();
	int get();
};
Lifo::Lifo() {
	head.next = NULL;
}
void Lifo::put(int data_value) {
	
	//creating new node
	lifo_node* add = new lifo_node;
	add->data = data_value; 
	cout << " put " << add->data << " in our queue " << endl;
	//pointer on NULL to prevent random number
	add->next = head.next;
	//in new element we want have pointer to the first element of a list
	head.next = add;
}

#define LIST_EMPTY (-1) //assuming positive values
int Lifo::get() {
	int get_value;
	if (head.next){
		get_value = head.next->data;
		lifo_node *temp_next = head.next->next;
		delete head.next;
		head.next = temp_next;
	}
	else {
		return LIST_EMPTY;
	}
	return get_value;
}

int main() {
	
	Lifo Queue;
	for (int i = 0; i <= 10; i++) {
		Queue.put(i);
	}
	for (int i = 0; i <= 11; i++) {
		cout << Queue.get() << endl;
	}
	return 0;
}
