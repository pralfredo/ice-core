function documents = preprocessText(textData)

% Tokenize the text.
documents = tokenizedDocument(textData);

% Lemmatize the words.
documents = addPartOfSpeechDetails(documents);
documents = normalizeWords(documents,Style="lemma");

% Erase punctuation.
documents = erasePunctuation(documents);

% Remove a list of stop words.
documents = removeStopWords(documents);
words = ["sub" "sup" "ice" "core" "greenland" "antarctica" "east" "antarctic"];
%words = ["sub" "sup" "ice" "core"];
%words = ["sub" "sup"];
documents = removeWords(documents, words);

% Remove words with 2 or fewer characters, and words with 15 or greater
% characters.
documents = removeShortWords(documents,2);
documents = removeLongWords(documents,20);

end