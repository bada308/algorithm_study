#include <stdio.h>
#include <string.h>

int main(){
    int tot[6] = {1,1,2,2,2,8};
    int sev[6];
    for (int i = 0; i < 6; i++)
    {
        scanf("%d",&sev[i]);
        printf("%d",tot[i] - sev[i]);
        printf(" ");
    }
    
}