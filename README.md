# dvdpack

Solve knapsack problem for your video life

## Usage

Guess you want to choose your video files
which keep within the total size of DVD single layer (4.7GB).

First, you make video folders and print size with du command.

What important are to:

- use unit of block size with 1KB (du -k)
- print total size with each specified directory (du -s).

```
$ du -sk */ep*
1653484 AmeKimi/ep01_03
35964   ChiiKawa/ep124
728548  ClassicStars/ep13
729600  Clevatess/ep02
566128  Danjoru/ep10
98192   GalaxyExpress/ep12
703704  HikaNatsu/ep02
776164  Kijin/ep15
577440  Mizuzokusei/ep03
730400  Mynoghra/ep01
1715772 Nageki/ep01_03
556768  Naruto/ep547
63644   ShibuyaHachi/ep37
1730764 SilentWitch/ep01_03
26568   SumikkoGurashi/ep11
730304  SummerPockets/ep14
726760  Takopi/ep04
1715436 TenseiSoushu/ep01_03
573632  TougenAnki/ep01
728724  TsuihoshaShokudo/ep01
1160464 WitchWatch/ep13_14
```

Then dvdpack tells how to pack your videos within DVD space.


```
$ du -sk */ep* |python -m dvdpack
4586996 AmeKimi/ep01_03 ChiiKawa/ep124 Danjoru/ep10 GalaxyExpress/ep12 Kijin/ep15 SummerPockets/ep14 Takopi/ep04
```

