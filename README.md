Documentation + installation guide for using Raylib with Python: https://electronstudio.github.io/raylib-python-cffi/

## Proposal

Team members: Jonas Welle, Henry Maddox, Joe C, Charles
Vision:
	A breakout game made with Raylib. In breakout, you play as a rectangle, which you can move with the arrow keys. A ball starts in the center of the screen, and immediately starts falling down. You have to make sure it doesn’t reach the bottom of the screen, which you do by moving to where the ball is, causing the ball to bounce up. After that, the ball may hit one of many blocks which may contain powerups and may give the player points, and then the ball falls back down. Once all the blocks are destroyed, the player wins.
Safe goal:
1.	The user can move a rectangle left and right with the arrow keys.
2.	A ball starts at the center of the screen, moving down. You can prevent it from reaching the bottom by letting the paddle touch the ball. The ball will then fall back down when it reaches the top of the screen, or a block. When the ball hits a block, the block disappears.
3.	When all of the blocks disappear, the game resets.
Stretch goal:
1.	Powerups are inside of certain blocks.
2.	Blocks disappearing increases your score.
3.	You can get a highscore which persists between games.
4.	Every time the player wins and the game resets, the pace of the game quickens.
Starting point/initial plans:
•	Each of the team members will have to download Raylib’s Python bindings and get that working, as well as some code editor like Visual Studio Code
•	We will have to either download some free sprites from online or draw our own. Either way, simply using shapes would be very boring
What we will take from GitHub: https://github.com/electronstudio/raylib-python-cffi
Which is actually bindings for this library: https://www.raylib.com/
Also we are unlikely to use starting code, except for Raylib itself. Of course, if we do end up using starting code, we will cite it.
