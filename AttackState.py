import pygame
import Character
#import Player
import Enemy
import Projectile
import Globals
import Victory
import Fireball

class AttackState:
    def update(self, char, camera, delta, platforms):
        pass

class gdeadState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.elapsed += delta
        if char.v[0] > 0:
            char.direction = 'right'
        else:
            char.direction = 'left'
        char.v = (0,0)
        char.attackReady = False
        char.dead = True
        
        if char.elapsed > char.RATE:
            if True:
                if char.deathCounter >= 5:
                    Globals.State.gargs.remove(char)
                elif char.direction == 'right':
                    if char.deathCounter == 11 or char.deathCounter == 12:
                        char.image = char.deathFRAMES[2]
                    else:
                        char.image = char.deathFRAMES[3]
                elif char.direction == 'left':
                    if char.deathCounter == 11 or char.deathCounter == 12:
                        char.image = char.deathFRAMES[0]
                    else:
                        char.image = char.deathFRAMES[1]
                char.deathCounter += 1
                #char.image = char.FRAMES[char.frame]
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            char.elapsed = 0

class gRunState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.elapsed += delta
        if char.elapsed > char.RATE:
            #update position
            if char.p[0] - char.xInitial < 0:
                diff = -(char.p[0] - char.xInitial)
            else:
                diff = char.p[0] - char.xInitial
            if diff > char.travelDistance:
                char.v = (-char.v[0],0)
                if char.direction == 'right':
                    char.direction = 'left'
                else:
                    char.direction = 'right'
            char.p = (char.p[0] + char.v[0]*char.elapsed,char.p[1])
            #update animation
            if char.direction == 'left':
                if char.frame >= char.numframes - 1:
                    char.frame = 0
                else:
                    char.frame += 1
            elif char.direction == 'right':
                if char.frame >= (char.numframes * 2 - 1) or char.frame < char.numframes:
                    char.frame = char.numframes
                elif char.frame < (char.numframes*2 - 1):
                    char.frame += 1
            char.image = char.FRAMES[char.frame]
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            char.elapsed = 0
                

class gRunDamageState(AttackState):
    def update(self,char,camera,delta,platforms):

        char.elapsed += delta
        if (char.damageCounter < 10 and char.damageCounter > 0):
            char.invincible = True
            char.attackReady = False
        else:
             char.invincible = False
             char.damageCounter = 0 
             if not char.player == 1:
                 char.attackReady = True
             return

        if char.elapsed > char.RATE:
            #update position
            if char.p[0] - char.xInitial < 0:
                diff = -(char.p[0] - char.xInitial)
            else:
                diff = char.p[0] - char.xInitial
            if diff > char.travelDistance:
                char.v = (-char.v[0],0)
                if char.direction == 'right':
                    char.direction = 'left'
                else:
                    char.direction = 'right'
            char.p = (char.p[0] + char.v[0]*char.elapsed,char.p[1])
            if (char.damageCounter < 10 and char.damageCounter > 0):
                #char.invincible = True
                if char.damageCounter % 2 == 0:
                    char.image = char.dmgFRAMES[2] #the blank
                else:
                    if char.direction == 'left': #and char.rightkey == 1 and char.leftkey == 0:
                        if char.frame >= char.numframes - 1:
                            char.frame = 0
                        else:
                            char.frame += 1
                    elif char.direction == 'right':# and char.leftkey == 1 and char.rightkey == 0:
                        if char.frame >= (char.numframes * 2 - 1) or char.frame < char.numframes:
                            char.frame = char.numframes
                        elif char.frame < (char.numframes*2 - 1):
                            char.frame += 1
                    char.image = char.FRAMES[char.frame]
                char.damageCounter += 1
           
           
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            
            char.elapsed = 0

class deadState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.elapsed += delta
        char.v = (0,char.v[1])
        if char.elapsed > char.RATE:
            #if(char.land_delay < 2):
            if False:
                char.land_delay += 1
                if(char.direction == 'right'):
                    char.image = char.jumpFRAMES[1]
                else:
                    char.image = char.jumpFRAMES[4]
            else:
                char.attackReady = False
                if char.deathCounter >= 3:
                    #print "Some kind of death"
                    #print type(char)
                    if isinstance(char,Enemy.Enemy):
                        Globals.State.enemies.remove(char)
                    #elif isinstance(char,Jock.Jock):
                    #    Globals.State.jocks.remove(char)
                    elif isinstance(char,Enemy.Boss):
                        Globals.State = Victory.Victory()
                    else:
                        Globals.State.jocks.remove(char)
                elif char.direction == 'right':
                    char.image = char.deathFRAMES[1]
                elif char.direction == 'left':
                    char.image = char.deathFRAMES[0]
                char.deathCounter += 1
                #char.image = char.FRAMES[char.frame]
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            #char.jumpVelSet = False
            char.jump_delay = 0
            char.elapsed = 0
        char.platCollide(camera,delta,platforms)

class StillBambiState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.elapsed+= delta
        char.v = (0,0)
        char.invincible = True
        if char.elapsed > char.RATE:
            if char.bambiCounter < 3:
                if char.direction == 'right':
                    char.image = char.BAMBI_FRAMES[0]
                else:
                    char.image = char.BAMBI_FRAMES[3]
            elif char.bambiCounter < 6:
                if char.direction == 'right':
                    char.image = char.BAMBI_FRAMES[1]
                else:
                    char.image = char.BAMBI_FRAMES[4]
            elif char.bambiCounter < 9:
                if char.direction == 'right':
                    char.image = char.BAMBI_FRAMES[2]
                else:
                    char.image = char.BAMBI_FRAMES[5]
            elif char.bambiCounter < 12:
                if char.direction == 'right':
                    char.image = char.BAMBI_FRAMES[1]
                else:
                    char.image = char.BAMBI_FRAMES[4]
            elif char.bambiCounter < 15:
                if char.direction == 'right':
                    char.image = char.BAMBI_FRAMES[2]
                else:
                    char.image = char.BAMBI_FRAMES[5]
            else:#done with bambi eat animation, set to stop coming in here
                if not char.health == 210:
                    char.health += 40
                char.gotBambi = False
                char.invincible = False
                char.bambiCounter = 0
            char.bambiCounter += 1
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            char.jumpVelSet = False
            char.jump_delay = 0
            char.elapsed = 0
        char.platCollide(camera,delta,platforms)
        
class RunBambiState(AttackState):
    def update(self,char,camera,delta,platforms):
        fred = 2

class StillState(AttackState):
    def update(self, char, camera,delta,platforms):

        char.elapsed += delta
        char.v = (0,char.v[1])
        if char.elapsed > char.RATE:
            #if(char.land_delay < 2):
            if False:
                char.land_delay += 1
                if(char.direction == 'right'):
                    char.image = char.jumpFRAMES[1]
                else:
                    char.image = char.jumpFRAMES[4]
            else:
   
                if char.direction == 'right':
                    char.image = char.stillFRAMES[0]
                elif char.direction == 'left':
                    char.image = char.stillFRAMES[1]
                #char.image = char.FRAMES[char.frame]
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            char.jumpVelSet = False
            char.jump_delay = 0
            char.elapsed = 0
        char.platCollide(camera,delta,platforms)

class RunState(AttackState):        
    #does platform collision then
    #sets char.image to appropriate frame based on:
    #if he just landed or if hes been on the ground and is just running
    #NOTE: should be player/enemy independent but it assumes that enemy has
    #jumpFrames and numframes AND RIGHTKEY/LEFTKEY etc, everything player has
    def update(self,char,camera,delta,platforms):

        char.elapsed += delta
        if(char.v[0] > 0):
            char.direction = 'right'
        else:
            char.direction = 'left'
        if char.elapsed > char.RATE:
        #if True:
            #char.platCollide(camera,char.elapsed,platforms) #NEED TO FIX TO BE PLAYER ENEMY INDEPENDENT 
            #if(char.land_delay < 2):
            if False:
                char.land_delay += 1
                if(char.direction == 'right'):
                    char.image = char.jumpFRAMES[1]
                else:
                    char.image = char.jumpFRAMES[4]
            else:
                if (char.rightkey == 1) and (char.leftkey == 0):
                    char.v = (char.runspeed,char.v[1])
                    char.direction = 'right'
                elif (char.leftkey == 1) and (char.rightkey == 0):
                    char.v = (-char.runspeed,char.v[1])
                    char.direction = 'left'
                elif char.leftkey and char.rightkey:
                    char.v = (0,char.v[1])
                if char.direction == 'right' and char.rightkey == 1 and char.leftkey == 0:
                    if char.frame >= char.numframes - 1:
                        char.frame = 0
                    else:
                        char.frame += 1
                elif char.direction == 'left' and char.leftkey == 1 and char.rightkey == 0:
                    if char.frame >= (char.numframes * 2 - 1) or char.frame < char.numframes:
                        char.frame = char.numframes
                    elif char.frame < (char.numframes*2 - 1):
                        char.frame += 1
            char.image = char.FRAMES[char.frame]
           
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            char.jumpVelSet = False
            char.jump_delay = 0
            char.elapsed = 0
        char.platCollide(camera,delta,platforms) #NEED TO FIX TO BE PLAYER ENEMY INDEPENDENT 

class JumpState(AttackState):
    #assumes char.grounded is 0 during crouching?
    #so if character is not grounded, it comes to here, then only does the crouching
    #if the jump delay is < 1, otherwise player is still not grounded, but does the in air
    #animation. So, grounded must be set to 0 as soon as the jump button is pressed even though
    #he is still on the ground for one more frame
    def update(self,char,camera,delta,platforms):
        #print "self.grounded is before: " + str(char.grounded)
        
        #print "self.grounded is after: " + str(char.grounded)
        char.elapsed += delta
        if char.elapsed > char.RATE:
        #if True:
            #char.platCollide(camera,char.elapsed,platforms) #NEED TO FIX TO BE f ENEMY INDEPENDENT
            #if (char.jump_delay < 1):
            #    if char.direction == 'right':
            #        char.image = char.jumpFRAMES[char.jump_delay + 1]
            #    else:
            #        char.image = char.jumpFRAMES[char.jump_delay + 4]
            #    char.jump_delay += 1
            #    char.rect = char.image.get_rect()
            #    char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            #else:
            if True:
                #if(char.jumped):
                    #char.v = (char.v[0],-370)
                    #char.v = (char.v[0],char.jumpspeed)
                    #char.jumped = 0
                if(char.direction == 'right'):
                    char.image = char.FRAMES[1]
                else:
                    char.image = char.FRAMES[char.numframes+1]
            #if(char.v[0] > 0):
            #    char.direction = 'right'
            #else:
            #    char.direction = 'left'

#these next lines handle lateral movement while in the air
                if (char.rightkey == 1) and (char.leftkey == 0):
                    char.v = (char.runspeed,char.v[1])
                    char.direction = 'right'
                elif (char.leftkey == 1) and (char.rightkey == 0):
                    char.v = (-char.runspeed,char.v[1])
                    char.direction = 'left'
                else:
                    char.v = (0,char.v[1])
            char.elapsed = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            char.land_delay = 0
            char.jump_delay = 0
        char.platCollide(camera,delta,platforms) #NEED TO FIX TO BE f ENEMY INDEPENDENT

class StillAttackState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.v = (0,char.v[1])
        
        char.elapsed += delta
        if char.elapsed > char.RATE:
        #if True:
            if char.attackDuration < char.numAttackFrames: #this counter is number of attack frames, change from hardcoded
                if char.attackDuration == 1:
                    char.attackSound.play() 
                if char.direction == 'right':
                    char.image = char.attackFRAMES[char.attackDuration]
                else:
                    char.image = char.attackFRAMES[char.attackDuration+2]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                char.attackDuration += 1
                char.slapEnemies(camera,delta,platforms)
            else: #now done with attack, set variables to stop coming in here
                char.isAttacking = 0
                char.attackDuration = 0
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms) #SEE ABOVE

class SparkleAttackState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.v = (0,0)
        if char.sparkleSoundPlayed == 0:
            char.sparkleSound.play()
            char.sparkleSoundPlayed = 1
        print char.attackDuration
        if char.elapsed < .4:
            if char.direction == 'right':
                    char.image = char.sparkleFrames[0]
            else:
                    char.image = char.sparkleFrames[2]
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.elapsed += delta
        if char.elapsed > .4:
        #if True:
            if char.attackDuration < char.numAttackFrames: #this counter is number of attack frames, change from hardcoded
                if char.attackDuration == .5:
                    print "Bob"
                    #char.attackSound.play() 
                if char.direction == 'right':
                    char.image = char.sparkleFrames[0]
                else:
                    char.image = char.sparkleFrames[2]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                char.attackDuration += 1
            else: #now done with attack, set variables to stop coming in here
                char.isSparkling = 0
                char.attackDuration = 0
                char.sparkleCloud = 10
                char.sparkleFireSound.play()
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms) #SEE ABOVE

class ShockwaveAttackState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.v = (0,char.v[1])
        char.elapsed += delta
        if char.elapsed > char.RATE:
        #if True:
            if char.attackDuration < 3: #this counter is number of attack frames, change from hardcoded
                #if char.attackDuration == 1:
                    #char.attackSound.play()
                #if char.isWolf == 0 and char.player==0:
                if True:
                    if not  char.madeWave:
                        char.madeWave = True
                        if char.direction == 'right':
                            wave = Projectile.Projectile((char.p[0] + char.image.get_width(), char.p[1] + char.image.get_height()-23),(150,0))
                            Globals.State.projectiles.append(wave)
                        else:
                            wave = Projectile.Projectile((char.p[0], char.p[1] + char.image.get_height()-23),(-150,0))
                            Globals.State.projectiles.append(wave)
                    if char.direction == 'right':
                        char.image = char.normalAttackFRAMES[char.attackDuration]
                    else:
                        char.image = char.normalAttackFRAMES[char.attackDuration+3]
                #if char.isWolf == 1:
                #    if char.direction == 'right':
                #        char.image = char.wolfAttackFRAMES[char.attackDuration]
                #    else:
                #        char.image = char.wolfAttackFRAMES[char.attackDuration+3]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                char.attackDuration += 1
                #char.slapEnemies(camera,delta,platforms)
            else: #now done with attack, set variables to stop coming in here
                char.isAttacking = 0
                char.attackReady = True
                char.attackDuration = 0
                char.madeWave = False
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms) #SEE ABOVE
        
class SparkledState(AttackState):
    def update(self,char,camera,delta,platforms):
        print "In sparkle"
        Globals.State.player.invincible = True
        char.v = (0,0)
        char.elapsed += delta
        if char.elapsed > char.blindLength:
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.inSparkle = 0
            Globals.State.player.invincible = False
        char.rect = char.image.get_rect()
        char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms) #SEE ABOVE

class SmashAttackState(AttackState):
    def update(self,char,camera,delta,platforms):
        #char.v = (0,char.v[1])
        char.elapsed += delta
        if char.elapsed > char.RATE*2.2 and char.attackDuration < 3 or char.elapsed > 0.6 and char.attackDuration >= 3:
        #if True:
            if char.attackDuration == 2: 
                if char.direction == 'right':
                    char.v = (200, -250)
                else:
                    char.v = (-200, -250)
            if ((char.attackDuration == 3 or char.attackDuration == 4) and char.elapsed > 0.6) or char.attackDuration < 3:
                if char.isWolf == 0 and char.player==0:
                    if char.direction == 'right':
                        char.image = char.jumpAttackFRAMES[char.attackDuration]
                    else:
                        char.image = char.jumpAttackFRAMES[char.attackDuration+5]
                if char.attackDuration == 4:
                    char.v = (0,0)
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                char.attackDuration += 1
                #char.slapEnemies(camera,delta,platforms)
            else: #now done with attack, set variables to stop coming in here
                char.isAttacking = 0
                char.attackReady = True
                char.attackDuration = 0
                char.jumping = False
                char.madeWave = False
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms) #SEE ABOVE


class SlashAttackState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.v = (0,char.v[1])
        char.elapsed += delta
        if char.elapsed > char.RATE:
        #if True:
            if char.attackDuration < 3: #this counter is number of attack frames, change from hardcoded
                #if char.attackDuration == 1:
                    #char.attackSound.play()
                if char.direction == 'right':
                    char.image = char.wolfAttackFRAMES[char.attackDuration]
                else:
                    char.image = char.wolfAttackFRAMES[char.attackDuration+2]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                char.attackDuration += 1
            else: #now done with attack, set variables to stop coming in here
                char.isAttacking = 0
                char.attackReady = True
                char.attackDuration = 0
                char.madeWave = False
                char.madeFire = False
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms) #SEE ABOVE

class FireAttackState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.v = (0,char.v[1])
        char.elapsed+=delta
        if char.elapsed > char.RATE:
 #           print char.madeFIRE
            if char.madeFIRE == False:
                char.madeFIRE = True
                if char.direction == 'right':
                    char.fire = Fireball.Fireball((char.p[0]+20+char.image.get_width(),char.p[1]+40),(180,0))
                else:
                    char.fire = Fireball.Fireball((char.p[0]-20,char.p[1]+40),(-180,0))
                Globals.State.projectiles.append(char.fire)
            if char.attackDuration < 4:
                if char.direction == 'right':
                    char.image = char.fireFRAMES[int(char.attackDuration/2)+2]
                else:
                    char.image = char.fireFRAMES[int(char.attackDuration/2)]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]),int(char.p[1]))
                char.attackDuration +=1
            else:
#                print "am i here?"
                char.isAttacking = 0
                char.attackReady = True
                char.attackDuration = 0
                char.madeFIRE = False
            char.elapsed = 0
        char.platCollide(camera,delta,platforms)

class WolfTransState(AttackState):
    def update(self, char, camera,delta,platforms):
        char.v = (0,0)
        char.elapsed += delta
        Globals.State.player.v = (0,0)
        Globals.State.player.paused = True
        #print char.transCounter
        if char.elapsed > .5:
            if char.transCounter < 4: #this counter is number of trans frames
                if char.transCounter == 1 or char.transCounter == 0:
                    if char.direction == 'right':
                        char.image = char.transFRAMES[0]
                    else:
                        char.image = char.transFRAMES[2]
                elif char.transCounter == 2 or char.transCounter == 3:
                    if char.direction == 'right':
                        char.image = char.transFRAMES[1]
                    else:
                        char.image = char.transFRAMES[3]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                char.transCounter += 1
            else: #now done with trans, set variables to stop coming in here
                char.transCounter = 7
                char.attackReady = True
                #print "Trans done"
                char.damageCounter = 0
                Globals.State.player.paused = False
            char.elapsed = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            #print "size after slap: " + str(char.image.get_width()) + ", " + str(char.image.get_height())
        char.platCollide(camera,delta,platforms) #SEE ABOVE
        #print "char.rect.topleft = " + str(char.rect.topleft) + "\nchar.p = " + str(char.p)



class RunAttackState(AttackState):
    def update(self, char, camera,delta,platforms):
        char.elapsed += delta
        #middle = (char.rect.topleft[0] + char.image.get_width()/2, char.rect.topleft[1] + char.image.get_height()/2)
        if char.elapsed > char.RATE - .05:
            #print "size before slap: " + str(char.image.get_width()) + ", " + str(char.image.get_height())
        #if True:
            if char.attackDuration < char.numAttackFrames: #this counter is number of attack frames, change from hardcoded
                if char.attackDuration == 1 and char.player==1:
                    char.attackSound.play() 
                if char.direction == 'right':
                    char.image = char.attackFRAMES[char.attackDuration]
                else:
                    char.image = char.attackFRAMES[char.attackDuration+char.numAttackFrames]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                #char.rect.topleft = (middle[0] - char.image.get_width()/2, middle[1] - char.image.get_height()/2)
                char.attackDuration += 1
                if char.player == 1:
                    char.slapEnemies(camera,delta,platforms)
                else:
                    char.slapPlayer(camera,delta,platforms)
            else: #now done with attack, set variables to stop coming in here
                char.isAttacking = 0
                char.attackDuration = 0
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            #print "size after slap: " + str(char.image.get_width()) + ", " + str(char.image.get_height())
        char.platCollide(camera,delta,platforms) #SEE ABOVE
        #print "char.rect.topleft = " + str(char.rect.topleft) + "\nchar.p = " + str(char.p)

class JumpAttackState(AttackState):
    def update(self,char,camera,delta,platforms):

        char.elapsed += delta
        if char.elapsed > char.RATE - .05:
        #if True:
            if char.attackDuration < char.numAttackFrames: #this counter is number of attack frames, change from hardcoded
                if char.attackDuration == 1:
                    char.attackSound.play() 
                if char.direction == 'right':
                    char.image = char.jumpAttackFRAMES[0]
                else:
                    char.image = char.jumpAttackFRAMES[1]
                char.rect = char.image.get_rect()
                char.rect.topleft = (int(char.p[0]), int(char.p[1]))
                char.attackDuration += 1
                char.slapEnemies(camera,delta,platforms)
            else: #now done with attack, set variables to stop coming in here
                char.isAttacking = 0
                char.attackDuration = 0
            char.elapsed = 0
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms) #SEE ABOVE

class StillDamageState(AttackState):
    def update(self,char,camera,delta,platforms):
        char.v = (0,char.v[1])
        char.elapsed += delta
        if (char.damageCounter < 8 and char.damageCounter > 0):
            char.invincible = True

        if char.elapsed > char.RATE -.05:
        #if True:
            if char.damageCounter < 8 and char.damageCounter > 0:#will flash 4 times, not frame dependent just a counter
                #char.invincible = True
                if char.damageCounter % 2 == 0: #every other make image blank
                    char.image = char.dmgFRAMES[2] #need to make a blank image
                elif char.direction == "right": #every other show correct direction dmg frame
                    char.image = char.dmgFRAMES[0]
                else:
                    char.image = char.dmgFRAMES[1]
                char.damageCounter += 1
            else:
                char.invincible = False
                char.damageCounter = 0
            char.elapsed = 0
            #char.jumpVelSet = False
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms)

class RunDamageState(AttackState):
    def update(self,char,camera,delta,platforms):

        char.elapsed += delta
        if (char.damageCounter < 8 and char.damageCounter > 0):
            char.invincible = True


        if char.elapsed > char.RATE -.05:
        #if True:
            if (char.rightkey == 1) and (char.leftkey == 0):
                char.v = (char.runspeed,char.v[1])
                char.direction = 'right'
            elif (char.leftkey == 1) and (char.rightkey == 0):
                char.v = (-char.runspeed,char.v[1])
                char.direction = 'left'
            elif char.leftkey and char.rightkey:
                char.v = (0,char.v[1])
            #if char.player == 0:
            #    print "Enemy in dmg run state!"
            if (char.damageCounter < 8 and char.damageCounter > 0):
                #char.invincible = True
                if char.damageCounter % 2 == 0:
                    char.image = char.dmgFRAMES[2] #the blank
                else:
                    if char.direction == 'right': #and char.rightkey == 1 and char.leftkey == 0:
                        if char.frame >= char.numframes - 1:
                            char.frame = 0
                        else:
                            char.frame += 1
                    elif char.direction == 'left':# and char.leftkey == 1 and char.rightkey == 0:
                        if char.frame >= (char.numframes * 2 - 1) or char.frame < char.numframes:
                            char.frame = char.numframes
                        elif char.frame < (char.numframes*2 - 1):
                            char.frame += 1
                    char.image = char.FRAMES[char.frame]
                char.damageCounter += 1
            else:
                char.invincible = False
                char.damageCounter = 0 
                if not char.player == 1:
                    char.attackReady = True
           
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
            char.jumpVelSet = False
            char.jump_delay = 0
            char.elapsed = 0
        char.platCollide(camera,delta,platforms)
        
class JumpDamageState(AttackState):
    def update(self,char,camera,delta,platforms):

        char.elapsed += delta
        if (char.damageCounter < 8 and char.damageCounter > 0):
            char.invincible = True

        if char.elapsed > char.RATE -.05:
        #if True:
            if char.damageCounter < 8 and char.damageCounter > 0:#will flash 4 times, not frame dependent just a counter 
                #char.invincible = True
                if char.damageCounter % 2 == 0: #every other make image blank
                    char.image = char.dmgFRAMES[2] #need to make a blank image
                elif char.direction == "right": #every other show correct direction dmg frame
                    char.image = char.dmgFRAMES[0]
                else:
                    char.image = char.dmgFRAMES[1]
                char.damageCounter += 1
            else:
                char.invincible = False
                char.damageCounter = 0
            char.elapsed = 0
            char.jumpVelSet = False
            char.land_delay = 0
            char.jump_delay = 0
            char.rect = char.image.get_rect()
            char.rect.topleft = (int(char.p[0]), int(char.p[1]))
        char.platCollide(camera,delta,platforms)

