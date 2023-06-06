#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

const int BLOCK_SIZE = 512;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    BYTE buffer[BLOCK_SIZE];
    int count = 0;
    string filename = malloc(8);
    FILE *img = NULL;
    // ここまでok
    while (fread(&buffer, sizeof(BYTE), BLOCK_SIZE, file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg", count);
            img = fopen(filename, "w");
            count++;
        }
        if (img != NULL)
        {
            fwrite(&buffer, sizeof(BYTE), BLOCK_SIZE, img);
        }
    }
    free(filename);
    fclose(file);
    fclose(img);
}