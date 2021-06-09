import React, { useState } from 'react';
import { StyleSheet, Text, View, SafeAreaView, TextInput, Button } from 'react-native';
import Genetic from './Genetic'

export default function App() {
  const [a, setNumber] = useState (null)
  const [b, setNumber] = useState(null);
  const [c, setNumber] = useState(null);
  const [d, setNumber] = useState(null);
  const [y, setNumber] = useState(null);
  const [result, setResult] = useState('click compute to calculate how many times the task was completed in 5 seconds ', []);

  function getRandomInRange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  return (
    <SafeAreaView>
      <View style={styles.container}>
        <TextInput style={styles.expression}
          onChangeText={setA}
          value={a}
          placeholder="a"
          keyboardType="numeric"
        />
        <Text style={styles.expression}>{'*x1 + '}</Text>
        <TextInput style={styles.expression}
         
          value={b}
          placeholder="b"
          keyboardType="numeric"
        />
        <Text style={styles.expression}>{'*x2 + '}</Text>
        <TextInput style={styles.expression}
        
          value={c}
          placeholder="c"
          keyboardType="numeric"
        />
        <Text style={styles.expression}>{'*x3 + '}</Text>
        <TextInput style={styles.expression}
         
          value={d}
          placeholder="d"
          keyboardType="numeric"
        />
        <Text style={styles.expression}>{'*x4 = '}</Text>
        <TextInput style={styles.expression}
         
          value={y}
          placeholder="Y"
          keyboardType="numeric"
        />
      </View>
      <Text style={styles.result}>
        {` Total cases completed =  ${result}`}
      </Text>
      <View style={styles.btn}>
        <Button
          title="Compute"
          color="white"
          onPress={() => {
            setResult(function testCases () {
              let totalCaseResult = 0;
              let starttime  = Date.now;
              while ((Date.now() - startTime) < 5000) {
                setNumber(getRandomInRange)
                new Genetic([a, b, c, d], y).solve()
                ++totalCaseResult ;
              }
              return totalCaseResult
            })
          }}
        />
        
      </View>

    </SafeAreaView>
  );
};


const styles = StyleSheet.create({
  container: {
    width: '90%',
    top: 200,
    flexDirection: 'row',
    alignSelf: 'center',
    alignItems: 'center',
    justifyContent: 'center',
  },
  expression: {
    fontSize: 25
  },
  result: {
    alignSelf: 'center',
    top: 269,
    fontSize: 25
  },
  time: {
    alignSelf: 'center',
    top: 320,
    fontSize: 22
  },
  btn: {
    justifyContent: 'center',
    alignItems: 'center',
    alignSelf: 'center',
    top: 300,
    height: 50,
    width: 150,
    backgroundColor: 'blue',
    borderRadius: 10,
  },
}); 