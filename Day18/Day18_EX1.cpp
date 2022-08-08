#include <iostream>
using namespace std;
/*
1)Snack에 int price - private
2)함수 getPrice(), setPrice() 구현 -public
3)함수 info()
:과자의 이름은 <포카칩>이고, 가격은 <1800>원입니다.
main에서 
Wafers.setPrice(1800);
Wafers.info();
*/
class Snack {
	private : // 밖에서 접근 X
		string name; //필드(클래스 안의 변수) : 객체의 데이터/부품 
		int price;
					 //메소드(클래스 안의 함수)
	// 퍼블릭으로 함수 하나 만들어서 프라이빗의 값을 수정하게 해 볼까..?
	public : // 밖에서 접근이 O
		
		void setName(string n); // 클래수 함수 선언
								// 밑에 있음!
		string getName();
		void ASMR();
		int getPrice();
		void setPrice(int n);
		void info();
};
//클래스 함수 구연
//반환타입 클래스명::함수명() <-- 이 클래스의 함수다
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
	cout << "바삭바삭" << endl;
}
void Snack::info() {
	cout << "과자의 이름은 " << name << "이고, 가격은 "
		<< price << "원입니다." << endl;

}
int main() {
	Snack Wafers;
	Wafers.setName("포카칩");
	//Wafers.name = "웨하스";
	cout << Wafers.getName() << endl; // endl = \n
	void ASMR();
	Wafers.setPrice(1800);
	Wafers.info();

	return 0;
}