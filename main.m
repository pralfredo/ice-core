function documents = main(total)
documents = preprocessText(total);
bag = bagOfWords(documents);
numDocuments = numel(documents);
cvp = cvpartition(numDocuments,'HoldOut',0.1);
documentsTrain = documents(cvp.training);
documentsValidation = documents(cvp.test);
bag = bagOfWords(documentsTrain);
rng("default")
numTopics = 6;
mdl = fitlda(bag,numTopics,Verbose=0);
figure
t = tiledlayout("flow");
title(t,"LDA Topics")
for i = 1:numTopics
nexttile
wordcloud(mdl,i);
title("Topic " + i)
end
topicMixtures = transform(mdl,documents);
for i = 1:numTopics
top = topkwords(mdl,5,i);
topWords(i) = join(top.Word,", ");
end
figure
bar(topicMixtures(1,:))
xlabel("Topic")
xticklabels(topWords);
ylabel("Probability")
title("Document Topic Probabilities")
end