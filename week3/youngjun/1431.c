//시리얼 번호

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS

int N;

void sort(char a[],char b[]){
    char temp[50];
    int num_a,num_b = 0;
    char t[50],p[50];

    if (strlen(a) > strlen(b))
    {
        strcpy(temp,a);
        strcpy(a,b);
        strcpy(b,temp);
    }

    if (strlen(a) == strlen(b))
    {
        for (int i = 0; i < strlen(a); i++)
        {
            if (a[i] > '0' && a[i] <= '9')
            {
                strcpy(&t[i],&a[i]);
                num_a += atoi(&t[i]);
            }
            if (b[i] > '0' && b[i] <= '9')
            {
                strcpy(&p[i],&b[i]);
                num_b += atoi(&p[i]);
            }
        }
        if (num_a > num_b)
        {
            strcpy(temp,a);
            strcpy(a,b);
            strcpy(b,temp);
        }
        else if (num_a == num_b)
        {
            for (int j = 0; j < strlen(a); j++)
            {
                if (a[j] > b[j])
                {
                    strcpy(temp,a);
                    strcpy(a,b);
                    strcpy(b,temp);

                    break;
                }
                if (a[j] < b[j])
                {
                    break;
                }
                
                
            }
            
        }     
    }
    else return;
    
}

int main(){
    scanf("%d\n",&N);
    //2차배열 arr 동적할당
    char** arr;
    arr = (char**)malloc(sizeof(char*)*N);
    for(int i = 0; i < N; i++)
    {
        arr[i] = (char*) malloc (sizeof(char)*50);
        scanf(" %s",arr[i]);
    }
    //

    for (int n1 = 0; n1 < N-1; n1++)
    {
        for (int n2 = n1+1; n2 < N; n2++)
        {
            sort(arr[n1],arr[n2]);
        }
        
    }
    

    for (int j = 0; j < N; j++)
    {
        printf("\n%s",arr[j]);
    }
    //동적할당 해제
    for (int l = 0; l < N; l++)
    {
        free(arr[l]);
    }
    free(arr);
    //
    return 0;
}