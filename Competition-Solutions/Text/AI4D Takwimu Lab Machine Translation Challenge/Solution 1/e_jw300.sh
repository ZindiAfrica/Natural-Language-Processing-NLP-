#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# !! Python 3.7 is required

cd $HOME/solution/data

pip3 install mtdata

mkdir fon ewe

mtdata get -l fr-fon -tr JW300 -o ./fon

mtdata get -l fr-ee -tr JW300 -o ./ewe

python3 jw300.py

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

