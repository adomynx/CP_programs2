import java.util.Scanner;

class wertyu{
    public static void main(String arg[]){
        Scanner sc=new Scanner(System.in);
        String str,keyboard;
        int len;
        keyboard="`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./";
        while(sc.hasNext()){
            str=sc.nextLine();
            len=str.length();
            for(int i=0;i<len;i++){
                if(str.charAt(i)==' '){
                    System.out.println(" ");}
                else{
                    System.out.print(keyboard.charAt(keyboard.indexOf(str.charAt(i))-1));
                }
                
            }
        System.out.println();
        }
    }
    
}