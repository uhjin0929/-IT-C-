#include <iostream>
using namespace std;
/*
1)Snack�� int price - private
2)�Լ� getPrice(), setPrice() ���� -public
3)�Լ� info()
:������ �̸��� <��īĨ>�̰�, ������ <1800>���Դϴ�.
main���� 
Wafers.setPrice(1800);
Wafers.info();
*/
class Snack {
	private : // �ۿ��� ���� X
		string name; //�ʵ�(Ŭ���� ���� ����) : ��ü�� ������/��ǰ 
		int price;
					 //�޼ҵ�(Ŭ���� ���� �Լ�)
	// �ۺ����� �Լ� �ϳ� ���� �����̺��� ���� �����ϰ� �� ����..?
	public : // �ۿ��� ������ O
		
		void setName(string n); // Ŭ���� �Լ� ����
								// �ؿ� ����!
		string getName();
		void ASMR();
		int getPrice();
		void setPrice(int n);
		void info();
};
//Ŭ���� �Լ� ����
//��ȯŸ�� Ŭ������::�Լ���() <-- �� Ŭ������ �Լ���
void Snack::setName(string n) {
	name = n;

}

void Snack::setPrice(int n) {
	price = n;
}
int Snack::getPrice() {
	return price;
}
string Snack::getName(){
	return name;
}
void Snack::ASMR() {
	cout << "�ٻ�ٻ�" << endl;
}
void Snack::info() {
	cout << "������ �̸��� " << name << "�̰�, ������ "
		<< price << "���Դϴ�." << endl;

}
int main() {
	Snack Wafers;
	Wafers.setName("��īĨ");
	//Wafers.name = "���Ͻ�";
	cout << Wafers.getName() << endl; // endl = \n
	void ASMR();
	Wafers.setPrice(1800);
	Wafers.info();

	return 0;
}