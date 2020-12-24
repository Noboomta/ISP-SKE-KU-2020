# Refactoring

## Code Chef

From CodeChef repository code: <https://github.com/hhhrrrttt222111/CodeChef>

consider this code from <https://github.com/hhhrrrttt222111/CodeChef/blob/main/Easy/Another%20Card%20Game%20Problem%20(CRDGAME3)/card.py>
(This is my commit at last week)

```python
    for i in range(round):
        a, b, *rest = [int(e) for e in input().split()]
        n1 = a//9
        n2 = b//9
        if(n1<n2):
            output.append(f"0 {count_num(a)}")
        else:
            output.append(f"1 {count_num(b)}")
```

- Refactoring signs.
  - variable name is not understandable.
  - can less the code by insert a condition into an if condition instead of creating a new variable.
  
```python
    for i in range(round):
        num1, num2, *rest = [int(e) for e in input().split()]
        if(num1//9 < num2//9):
            output.append(f"0 {count_num(num1)}")
        else:
            output.append(f"1 {count_num(num2)}")
```

consider this code from <https://github.com/OOP2020/pa3-Noboomta/blob/master/src/converter/Temperature.java>
(This is my PA3 from OOP class)

```java
    @Override
    public double convert(double amount, Unit fromUnit) {
        double fromCode = fromUnit.getValue();
        double hereCode = this.getValue();
        if (fromCode == 111){
            if (hereCode == 222){
                return amount + 273.15;
            }
            else if(hereCode == 333){
                return (amount * 9.0/5.0) + 32;
            }
        }
        else if(fromCode == 222){
            if(hereCode == 111){
                return amount - 273.15;
            }
            else if(hereCode == 333){
                return (amount - 273.15) * (9.0/5.0) + 32;
            }
        }
        else if(fromCode == 333){
            if(hereCode == 111){
                return (amount - 32.0)* (5.0/9.0);
            }
            else if(hereCode == 222){
                return (amount - 32.0)* (5.0/9.0) + 273.15;
            }
        }
        return amount;
    }
```

- Refactoring signs.
  - refactor the condition.
  - refactor the separating of the number in the condition.

- Coding style Error.
  - no space after ")".

```java
    @Override
    public double convert(double amount, Unit fromUnit) {
        double fromCode = fromUnit.getValue();
        double hereCode = this.getValue();
        switch(fromCode){
            case(111):
                if(hereCode == 222): return amount + 273.15;
                else if(hereCode == 333): return (amount * (9.0/5.0)) + 32;
            case(222):
                if(hereCode == 111): return amount - 273.15;
                else if(hereCode == 333): return ((amount - 273.15) * (9.0/5.0)) + 32;
            case(333):
                if(hereCode == 111): return (amount - 32.0) * (5.0/9.0);
                else if(hereCode == 222): return ((amount - 32.0) * (5.0/9.0)) + 273.15;
        }
        return amount;
    }
```

consider this code from <https://github.com/Noboomta/PA4/blob/master/src/sample/AllTask.java>
(This is my PA4 from OOP class)

```java
        /**
     * To return all task progress
     */
    public double getAllProgress() {
        double allProgress = 0;
        for (Task task : allTask) {
            allProgress += task.getProgress();
        }
        return allProgress / allTask.size();
    }
```

- Refactoring signs.
  - refactor the to not calculate in the return method.
  - move the calculate process to set in the class attribute.

```java
        /**
     * To return all task progress
     */
    public double getAllProgress() {
        this.setProgress();
        return this.allProgress;
    }

    /**
     * Set all progress.
     */
    public void setProgress(){
        double allProg = 0;
        for (Task task : allTask) {
            allProg += task.getProgress();
        }
        this.allProgress = allProg / allTask.size();
    }
```
