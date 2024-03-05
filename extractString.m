function list = extractString(documents)
list = [];
for x=1:53
if ~isempty(documents{x})
len = size(documents{x});
for y=1:len(1)
if ~isempty(documents{x}{y})
list = [list, documents{x}{y}];
end
end
end
end
end