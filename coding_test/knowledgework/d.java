package coding_test.knowledgework;

class Athlete{
  int num;
  double startingPlace;

  void setNumPlace(int n, double p){
    num = n;
    startingPlace = p;
    System.out.println("選手のゼッケン番号を"+num+"に、出発位置を"+startingPlace+"に設定しました。");
  }
  void show(){
    System.out.println("選手のゼッケン番号は"+num+"です。");
    System.out.println("出発位置は"+startingPlace+"です。");
  }
}

class Announce{
  public static void main(String[] args){
    Athlete michael = new Athlete();
    michael.setNumPlace(12, 423);
    michael.show();
  }
}