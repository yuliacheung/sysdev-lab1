#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main() {
    char *greeting = malloc(32);
    strcpy(greeting, "Hello, world!");
    printf("%s\n", greeting);

    free(greeting);
    greeting = NULL;   // 释放后立刻置空，避免后续误用

    // greeting[0] = 'J';   // 已删除：这里就是 use-after-free 的位置
    // printf("%s\n", greeting);

    return 0;
}
