package algo.Sorting;

public class InsertionSort {
	
	void sort(int arr[]){
		int n = arr.length;
		
		for(int i=0;i<n;i++){
			for(int j=i;j>0;j--){
				if(arr[j]<arr[j-1]){
					int temp=arr[j];
					arr[j]=arr[j-1];
					arr[j-1]=temp;
				}
				else
					break;
			}
		}
	}
	
	 static void printArray(int arr[])
	    {
	        int n = arr.length;
	        for (int i=0; i<n; ++i)
	            System.out.print(arr[i] + " ");
	 
	        System.out.println();
	    }
	 
	    // Driver method
	    public static void main(String args[])
	    {        
	        int arr[] = {12, 11, 13, 5, 6};
	 
	        InsertionSort ob = new InsertionSort();        
	        ob.sort(arr);
	         
	        printArray(arr);
	    }

}

