// Snake-Game-Team10.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "Snake.h"
#include "raylib.h"

#pragma once
//------------------------------------------------------------------------------------
// Program main entry point
//------------------------------------------------------------------------------------

Color green = { 173,204,96,255 };
Color darkgreen = { 43,51,24,255 };
int cellsize = 30;
int cellcount = 50;
typedef enum GameScreen { LOGO = 0, TITLE, GAMEPLAY, ENDING } GameScreen;

/******** Class Food for  ********/
class Food {
public:
    int PosX = rand() % cellsize;
    int PosY = rand() % cellsize;
    Texture2D texture;

    Food() {

        Image image = LoadImage("Graphics/Snake.png");
        ImageResizeNN(&image, 30, 30);
        texture = LoadTextureFromImage(image);
        UnloadImage(image);
    }

    ~Food() {
        UnloadTexture(texture);
    }

    void Draw() {
        DrawTexture(texture,PosX*cellsize,PosY*cellsize,WHITE);
    }
};
//------- End of Food class

int main(void) {

    // Initialization
   //---------------------------------------------------------

    const int screenWidth = 1000;
    const int screenHeight = 800;

    InitWindow(screenWidth, screenHeight, "Spicy Snake Game");

    Snake snake=Snake();
    Food food;

    bool pause = 0;
    int framesCounter = 0;
    GameScreen currentScreen = LOGO;


    SetTargetFPS(60);               // Set our game to run at 60 frames-per-second
    //----------------------------------------------------------
    double difficulty = 0.2;
    // Main game loop
    while (!WindowShouldClose())    // Detect window close button or ESC key
    {
        // Update
        //-----------------------------------------------------
        switch (currentScreen) {
        case LOGO: {
            framesCounter++;    // Count frames

            // Wait for 2 seconds (120 frames) before jumping to TITLE screen
            if (framesCounter > 120)
            {
                currentScreen = TITLE;
            }
        }break;
        case TITLE: {
            if (IsKeyPressed('1'))
            {
                difficulty = 0.3;
                currentScreen = GAMEPLAY;
            }
            else if (IsKeyPressed('2')) {
                difficulty = 0.2;
                currentScreen = GAMEPLAY;
            }
            else if (IsKeyPressed('3')) {
                difficulty = 0.1;
                currentScreen = GAMEPLAY;
            }
            else if (IsKeyPressed('4')) {
                difficulty = 0.05;
                currentScreen = GAMEPLAY; 
            }
        }break;
        case GAMEPLAY: {
            
            }break; 
         default:break;
        }
        
        //-----------------------------------------------------

        // Draw
        //-----------------------------------------------------
        BeginDrawing();
        ClearBackground(green); //coloring the background
        switch (currentScreen)
        {
        case LOGO: {
            DrawText("LOADING...", 350, 400, 60, GRAY);
        }break;
        case TITLE:
        {
            DrawText("Spicy Snake Game", 230, 20, 60, DARKGREEN);
            DrawText("Select which difficulty you want", 178, 300, 40, DARKGREEN);
            DrawText("1.Easy    2.Medium    3.Hard  4.Impossible", 297, 400, 20, DARKGREEN);
        } break;
        case GAMEPLAY:
        {
            if (IsKeyPressed(KEY_SPACE)) pause = !pause;
            if (!pause)
            {
                if (snake.eventTriggered(difficulty)) {
                    snake.update();
                }

                if (IsKeyPressed(KEY_RIGHT) && snake.x != -1) {
                    snake.x = 1;
                    snake.y = 0;
                }
                if (IsKeyPressed(KEY_LEFT) && snake.x != 1) {
                    snake.x = -1;
                    snake.y = 0;
                }if (IsKeyPressed(KEY_UP) && snake.y != 1) {
                    snake.x = 0;
                    snake.y = -1;
                }if (IsKeyPressed(KEY_DOWN) && snake.y != -1) {
                    snake.x = 0;
                    snake.y = 1;
                }
            }
            else framesCounter++;
            food.Draw();
            snake.Draw();
            // On pause, we draw a blinking message
            //if (pause && ((framesCounter / 30) % 2)) DrawText("PAUSED", 350, 200, 30, GRAY);
            //on Pause, we draw a message "paused"
            if (pause) DrawText("paused", 465, 400, 30, GRAY);
            //DrawFPS(10, 10);
        } break; 
        default:break; 
        }

        EndDrawing();
        //-----------------------------------------------------
    }

    // De-Initialization
    //---------------------------------------------------------
    CloseWindow();        // Close window and OpenGL context
    //----------------------------------------------------------

    return 0;
}
