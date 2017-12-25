// Program to perform a linear Search 

import java.util.Scanner;

public class LinearSearch{

    public static int search(int arr[], int num, int n){

        for (int i=0;i<n;i++){
        if (arr[i]==num)
            return i;
        }

        return -1;
        
        

    }

    public static void main(String args[]){
    
        Scanner sc= new Scanner(System.in);

        System.out.println("Please enter a number of elements : ");
        int n=sc.nextInt();
        int arr[]=new int[n];
        System.out.println("Please enter the elements: ");
        sc.nextLine();
        for (int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }

        System.out.println("Your Array");
        for(int i=0;i<n;i++)
            System.out.println(arr[i]);


        sc.nextLine();

        System.out.println("Enter the number to be searched : ");
        int num=sc.nextInt();
        int result = search( arr, num,n );
        if(result==-1)
            System.out.println("No not found!!");
        else
            System.out.println("Yayyyy Number found at "+ (result+1)+"th location");

    }




   

}
