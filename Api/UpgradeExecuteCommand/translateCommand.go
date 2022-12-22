package main

import (
	"fmt"
	"strings"
)

type highSearchingReturn struct {
	First  int
	Second int
}

type searchForExecuteReturn struct {
	SuccessStates bool
	Pointer       int
}

type getSelectorReturn struct {
	Selector string
	Pointer  int
}

type getPosUsed struct {
	Posx string
	Posy string
	Posz string
}

type getPosReturn struct {
	Position string
	Pointer  int
}

type detectBlockReturn struct {
	SuccessStates bool
	DetectString  string
	Pointer       int
}

func main() {
	fmt.Println(runFUNC("execute@p~~~kill@s"))
}

func runFUNC(command string) string {
	defer func() {
		if err := recover(); err != nil {
			// fmt.Printf("WARNING - %v\n", err)
		}
	}()
	// if some where work unexpected, err != nil
	return run(command)
}

func jumpSpace(command string, pointer int) int {
	for {
		if pointer >= len(command)-1 {
			return pointer
		} else if command[pointer] == ' ' || command[pointer] == '/' {
			pointer++ // pointer = pointer + 1
		} else {
			return pointer
		}
	}
}

func StringIndex(input string, searchingFor string, pointer int) int {
	find := strings.Index(input[pointer:], searchingFor)
	if find == -1 {
		return -1
	} else {
		return find + pointer
	}
}

func highSearching(command string, pointer int, input map[int]string) highSearchingReturn {
	List := map[int]map[int]int{}
	// example: List[0][1] = 2 -----> [ [1,2] ]
	// example: List[0][1] = 2 && List[1][1] = 2 -----> [ [1,2], [1,2] ]
	executeCount := 0
	for _, value := range input {
		find := StringIndex(command, value, pointer)
		if find != -1 {
			if List[executeCount] == nil {
				List[executeCount] = make(map[int]int)
			}
			List[executeCount][strings.Index(command[pointer:], value)] = len(value)
			executeCount++ // executeCount = executeCount + 1
		}
	}
	// List = [[command.find(i,pointer),len(i)] for i in input]
	minRecord := 2147483647
	location := 0
	for key1, value := range List {
		for key2 := range value {
			if key2 < minRecord {
				minRecord = key2
				location = key1
			}
		}
	}
	return highSearchingReturn{
		First:  minRecord + pointer,
		Second: List[location][minRecord],
	}
}

// while this FUNC return -1, then it seems that somewhere may cause wrong!
func getRightBarrier(command string, pointer int) int {
	for {
		quotationMark := StringIndex(command, "\"", pointer)
		barrier := StringIndex(command, "]", pointer)
		if quotationMark == -1 {
			return barrier
		} else if quotationMark < barrier {
			IndexAns := StringIndex(command, "\"", quotationMark+1)
			if IndexAns == -1 {
				return -1
			}
			pointer = StringIndex(command, "\"", quotationMark+1) + 1
		} else {
			return barrier
		}
	}
}

func joinMapToString(input map[int]string, Len int) string {
	output := ""
	if Len <= 0 {
		return output
	} else {
		pointer := -1
		for {
			pointer++ // pointer = pointer + 1
			if pointer > Len {
				break
			}
			output = output + input[pointer]
		}
		return output
	}
}

// while this FUNC return {"", -1}, then it seems that somewhere may cause wrong!
func searchForExecute(command string, pointer int) searchForExecuteReturn {
	pointer = jumpSpace(command, pointer)
	commandHeader := ""
	if pointer+7 > len(command)-1 {
		commandHeader = command[pointer:]
	} else {
		commandHeader = command[pointer : pointer+7]
	}
	commandHeader = strings.Replace(commandHeader, "E", "e", -1)
	commandHeader = strings.Replace(commandHeader, "X", "x", -1)
	commandHeader = strings.Replace(commandHeader, "C", "c", -1)
	commandHeader = strings.Replace(commandHeader, "U", "u", -1)
	commandHeader = strings.Replace(commandHeader, "T", "t", -1)
	if commandHeader == "execute" {
		return searchForExecuteReturn{
			SuccessStates: true,
			Pointer:       pointer + 7,
		}
	} else {
		return searchForExecuteReturn{
			SuccessStates: false,
			Pointer:       pointer,
		}
	}
}

func getSelector(command string, pointer int) getSelectorReturn {
	pointer = jumpSpace(command, pointer)
	if command[pointer] == "@"[0] {
		transit := highSearching(command, pointer, map[int]string{
			0: "@s",
			1: "@a",
			2: "@p",
			3: "@e",
			4: "@r",
			5: "@initiator",
			6: "@c",
			7: "@v",
		})
		selector := command[pointer : transit.First+transit.Second]
		pointer = jumpSpace(command, transit.First+transit.Second)
		if pointer >= len(command)-1 {
			return getSelectorReturn{Selector: selector, Pointer: pointer}
		} else if command[pointer] != '[' {
			return getSelectorReturn{Selector: selector, Pointer: pointer}
		} else {
			transit := getRightBarrier(command, pointer)
			if transit == -1 {
				return getSelectorReturn{Selector: "", Pointer: -1}
			}
			return getSelectorReturn{
				Selector: selector + command[pointer:transit+1],
				Pointer:  transit + 1,
			}
		}
	} else if command[pointer] == "\""[0] {
		transit := StringIndex(command, "\"", pointer+1)
		return getSelectorReturn{Selector: command[pointer : transit+1], Pointer: transit + 1}
	} else {
		transit := highSearching(command, pointer, map[int]string{0: " ", 1: "^", 2: "~"})
		return getSelectorReturn{
			Selector: command[pointer : transit.First+transit.Second-1],
			Pointer:  transit.First + transit.Second - 1,
		}
	}
}

// while this FUNC return {"", -1}, then it seems that somewhere may cause wrong!
func getPos(command string, pointer int) getPosReturn {
	pointer = jumpSpace(command, pointer)
	ans := getPosUsed{}
	repeatCount := 3
	for {
		repeatCount-- // repeatCount = repeatCount - 1
		if repeatCount < 0 {
			break
		}
		transit := highSearching(command, pointer+1, map[int]string{
			0: " ",
			1: "^",
			2: "~",
			3: "a", 4: "b", 5: "c", 6: "d", 7: "e", 8: "f", 9: "g", 10: "h", 11: "i", 12: "j", 13: "k", 14: "l",
			15: "m", 16: "n", 17: "o", 18: "p", 19: "q", 20: "r", 21: "s", 22: "t", 23: "u", 24: "v", 25: "w",
			26: "x", 27: "y", 28: "z",
			29: "A", 30: "B", 31: "C", 32: "D", 33: "E", 34: "F", 35: "G", 36: "H", 37: "I", 38: "J", 39: "K",
			40: "L", 41: "M", 42: "N", 43: "O", 44: "P", 45: "Q", 46: "R", 47: "S", 48: "T", 49: "U", 50: "V",
			51: "W", 52: "X", 53: "Y", 54: "Z",
		})
		successStates := false
		for _, value := range map[int]string{0: "~", 1: "^", 2: "0", 3: "1", 4: "2", 5: "3", 6: "4", 7: "5", 8: "6", 9: "7", 10: "8", 11: "9"} {
			if command[pointer] == value[0] {
				successStates = true
			}
		}
		if successStates == false {
			return getPosReturn{Position: "", Pointer: -1}
		}
		if repeatCount == 2 {
			ans.Posx = command[pointer:transit.First]
			pointer = jumpSpace(command, transit.First)
			continue
		}
		if repeatCount == 1 {
			ans.Posy = command[pointer:transit.First]
			pointer = jumpSpace(command, transit.First)
			continue
		}
		if repeatCount == 0 {
			ans.Posz = command[pointer:transit.First]
			pointer = jumpSpace(command, transit.First)
		}
	}
	return getPosReturn{
		Position: ans.Posx + " " + ans.Posy + " " + ans.Posz,
		Pointer:  pointer,
	}
}

// while this FUNC return {false, "", -1}, then it seems that somewhere may cause wrong!
func detectBlock(command string, pointer int) detectBlockReturn {
	pointer = jumpSpace(command, pointer)
	Header := ""
	if pointer+6 > len(command)-1 {
		Header = command[pointer:]
	} else {
		Header = command[pointer : pointer+6]
	}
	Header = strings.Replace(Header, "D", "d", -1)
	Header = strings.Replace(Header, "E", "e", -1)
	Header = strings.Replace(Header, "T", "t", -1)
	Header = strings.Replace(Header, "C", "c", -1)
	if Header == "detect" {
		save := getPos(command, jumpSpace(command, pointer+6))
		if save.Position == "" && save.Pointer == -1 {
			return detectBlockReturn{
				SuccessStates: false,
				Pointer:       -1,
			}
		}
		pos := save.Position
		startLocation := jumpSpace(command, save.Pointer)
		pointer := startLocation
		endLocation := StringIndex(command, " ", pointer)
		spaceLocation := StringIndex(command, " ", jumpSpace(command, endLocation+1))
		return detectBlockReturn{
			SuccessStates: true,
			DetectString:  " if block " + pos + " " + command[startLocation:endLocation] + " " + command[endLocation+1:spaceLocation],
			Pointer:       spaceLocation,
		}
	} else {
		return detectBlockReturn{
			SuccessStates: false,
			Pointer:       pointer,
		}
	}
}

func run(command string) string {
	ans := map[int]string{}
	pointer := -1
	repeatCount := 0
	for {
		repeatCount++ // repeatCount = repeatCount + 1
		pointer++     // pointer = pointer + 1
		markable := searchForExecute(command, pointer)
		if markable.SuccessStates == true {
			selector := getSelector(command, markable.Pointer)
			pos := getPos(command, selector.Pointer)
			if pos.Position == "" && pos.Pointer == -1 {
				// fmt.Printf("WARNING - Syntax error detected, occurring in \"%v\"[%v]\n", command, selector.Pointer)
				return command
			}
			detect := detectBlock(command, pos.Pointer)
			pointer = detect.Pointer - 1
			Selector := selector.Selector
			Position := pos.Position
			Detect := ""
			if detect.SuccessStates == true {
				Detect = detect.DetectString
			} else {
				Detect = ""
			}
			if Position == "~ ~ ~" {
				ans[repeatCount] = "as " + Selector + " at " + Selector + Detect + " "
			} else {
				ans[repeatCount] = "as " + Selector + " at " + Selector + " positioned " + Position + Detect + " "
			}
		} else {
			ans[repeatCount] = command[markable.Pointer:]
			break
		}
	}
	maxRecord := 0
	for key := range ans {
		if maxRecord < key {
			maxRecord = key
		}
	}
	if maxRecord <= 1 {
		return joinMapToString(ans, maxRecord)
	} else {
		ans[maxRecord] = "run " + ans[maxRecord]
		return "execute " + joinMapToString(ans, maxRecord)
	}
}
