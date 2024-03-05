function years = stringMaker(abs)
strings = [];
years = [];
for x=1:53
if ~isempty(abs{x})
len = size(abs{x});
for y=1:len(1)
if ~isempty(abs{x}{y})
strings = [strings, abs{x}{y}];
years = [years, x+1968];
end
end
end
end